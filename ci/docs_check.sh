#!/usr/bin/env bash
set -euo pipefail
REQUIRE_DOCS=$(awk '/require_update_on_api_change:/ {print $2}' config/project.yml)
if [[ "$REQUIRE_DOCS" == "true" ]]; then
  echo "Checking for docs/ADR updates on API change..."
  # Simple stub: if any .ts file in services/ or packages/ changed, require docs/ or artifacts/adr/ to be updated
  API_CHANGED=$(git diff --name-only origin/main | grep -E '^(services|packages)/.*\.ts$' || true)
  DOCS_CHANGED=$(git diff --name-only origin/main | grep -E '^(docs/|artifacts/adr/)' || true)
  if [[ -n "$API_CHANGED" && -z "$DOCS_CHANGED" ]]; then
    echo "API changed but no docs/ADR update detected. Please update documentation and ADRs."
    exit 1
  fi
fi
