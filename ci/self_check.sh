#!/usr/bin/env bash
set -euo pipefail

# Template Self-Check Script
# Verifies required template paths exist (template integrity only)

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REQUIRED_PATHS=(
  "$SCRIPT_DIR/../scripts/overlay/ci/config_eval.ts"
  "$SCRIPT_DIR/../scripts/overlay/ci/coverage.sh"
  "$SCRIPT_DIR/../scripts/overlay/ci/docs_check.sh"
  "$SCRIPT_DIR/../scripts/overlay/github/ci.yml"
  "$SCRIPT_DIR/../scripts/apply_overlay.sh"
  "$SCRIPT_DIR/../packages/feature-flags/index.ts"
  "$SCRIPT_DIR/../packages/otel-stubs/index.ts"
  "$SCRIPT_DIR/../services/example-service-ts/index.ts"
  "$SCRIPT_DIR/../services/example-service-ts/index.test.ts"
  "$SCRIPT_DIR/../docs/playbook.md"
  "$SCRIPT_DIR/../docs/prompts/00_CALIBRATION.md"
  "$SCRIPT_DIR/../docs/prompts/10_ATOMIC_TASK.md"
  "$SCRIPT_DIR/../docs/prompts/20_GUARDRAIL.md"
  "$SCRIPT_DIR/../docs/prompts/30_REVIEW.md"
)

missing=0
for path in "${REQUIRED_PATHS[@]}"; do
  if [ ! -e "$path" ]; then
    echo "Missing required path: $path"
    missing=1
  fi
done

if [ "$missing" -eq 0 ]; then
  echo "Template self-check PASSED: all required paths exist."
  exit 0
else
  echo "Template self-check FAILED: missing required paths."
  exit 1
fi
