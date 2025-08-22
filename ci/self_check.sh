#!/usr/bin/env bash
set -euo pipefail

# Template Self-Check Script
# Verifies required template paths exist (template integrity only)

REQUIRED_PATHS=(
  "scripts/overlay/ci/config_eval.ts"
  "scripts/overlay/ci/coverage.sh"
  "scripts/overlay/ci/docs_check.sh"
  "scripts/overlay/github/ci.yml"
  "scripts/apply_overlay.sh"
  "packages/feature-flags/index.ts"
  "packages/otel-stubs/index.ts"
  "services/example-service-ts/index.ts"
  "services/example-service-ts/index.test.ts"
  "docs/playbook.md"
  "docs/prompts/00_CALIBRATION.md"
  "docs/prompts/10_ATOMIC_TASK.md"
  "docs/prompts/20_GUARDRAIL.md"
  "docs/prompts/30_REVIEW.md"
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
