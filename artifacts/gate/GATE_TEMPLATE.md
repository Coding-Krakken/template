---
id: gate-GXXXX
type: gate
name: Descriptive Gate Name
requires:
  - artifact: path/to/required/artifact.md
  - metric: test.pass_rate >= 0.99
  - metric: security.critical_vulns == 0
  - metric: mutation.score >= 70  # Enforced via ci/check_mutation.py
  - review: privacy.signoff == true
evaluator: ci/policies/gates.rego
---

## Purpose

Explain the purpose of this gate.  Gates act as hard checkpoints in the
development process.  They ensure that critical evidence (tests, threat models,
security scans, performance results, privacy sign‑offs, etc.) exists and meets
defined criteria before work proceeds.

## Evidence Checklist

| Requirement | Evidence | Notes |
|------------|---------|------|
| **Artifact** | Provide the path to the required artifact in the repository | |
| **Metric** | Specify the metric and the target threshold (e.g., mutation.score ≥ 70, enforced via ci/check_mutation.py) | |
| **Review** | Indicate whether a manual review or sign‑off is required | |

Populate this section with links to the actual evidence once it is available.