#!/usr/bin/env bash
set -euo pipefail
REQUIRE_DOCS=$(awk '/require_update_on_api_change:/ {print $2}' config/project.yml)
if [[ "$REQUIRE_DOCS" == "true" ]]; then
  echo "Checking for docs/ADR updates on API change..."
  # TODO: Implement API change detection and docs/ADR check
fi
