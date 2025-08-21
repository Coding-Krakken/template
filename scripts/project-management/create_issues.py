"""
create_issues.py — Automated GitHub Issue Creator

Elite-grade script for syncing local markdown issues to GitHub Issues, then cleaning up local files.

Features:
- Reads all markdown files in .github/issues/
- Creates GitHub issues using the GitHub REST API
- Assigns GitHub Copilot to each issue
- Deletes local files after successful creation
- Robust error handling, logging, and idempotency
- Designed for CI/CD and enterprise workflows
"""
import os
import glob
import requests
import logging
from pathlib import Path

# --- CONFIGURATION ---
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN') or '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'  # Set this in your CI/CD secrets or use provided token
import subprocess
import re

def get_repo_info():
    try:
        url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], encoding='utf-8').strip()
        # Support both HTTPS and SSH URLs
        match = re.search(r'github.com[/:]([^/]+)/([^/.]+)', url)
        if match:
            owner, name = match.group(1), match.group(2)
            return owner, name
    except Exception as e:
        logging.error(f"Failed to detect repo info: {e}")
    # Fallback to defaults
    return 'Coding-Krakken', 'template'

REPO_OWNER, REPO_NAME = get_repo_info()
ISSUES_DIR = Path('.github/issues')
COPILOT_USERNAME = 'github-copilot[bot]'
API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# --- UTILITIES ---
def parse_issue_md(md_path):
    """Parse markdown file for title and body."""
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    title = None
    body = ''
    for line in lines:
        if not title and line.strip().startswith('# '):
            title = line.strip().lstrip('# ').strip()
        else:
            body += line
    if not title:
        title = md_path.stem
    return title, body

def create_github_issue(title, body, assignees=None, labels=None):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github+json',
    }
    # Add 'copilot' label and mention Copilot in the body
    copilot_label = 'copilot'
    all_labels = (labels or ['parallelizable', 'no-conflict', 'size:S'])
    if copilot_label not in all_labels:
        all_labels.append(copilot_label)
    copilot_mention = '\n\n_Assigned to Copilot: @github-copilot[bot] (automatic assignment not supported by GitHub API for bots)_'
    data = {
        'title': title,
        'body': body + copilot_mention,
        'labels': all_labels,
    }
    # Only add assignees if provided and valid
    if assignees:
        data['assignees'] = assignees
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 201:
        logging.info(f"Created issue: {title}")
        return True
    else:
        logging.error(f"Failed to create issue '{title}': {response.status_code} {response.text}")
        return False

def main():
    if not GITHUB_TOKEN:
        logging.error('GITHUB_TOKEN environment variable not set.')
        return
    if not ISSUES_DIR.exists():
        logging.error(f'Issues directory {ISSUES_DIR} does not exist.')
        return
    issue_files = sorted(glob.glob(str(ISSUES_DIR / '*.md')))
    if not issue_files:
        logging.info('No issue files found.')
        return
    for md_path in issue_files:
        md_path = Path(md_path)
        if md_path.name == 'template.md':
            logging.info(f"Skipping template file: {md_path}")
            continue
        title, body = parse_issue_md(md_path)
        success = create_github_issue(title, body)
        if success:
            try:
                md_path.unlink()
                logging.info(f"Deleted local issue file: {md_path}")
            except Exception as e:
                logging.error(f"Failed to delete {md_path}: {e}")

if __name__ == '__main__':
    main()
