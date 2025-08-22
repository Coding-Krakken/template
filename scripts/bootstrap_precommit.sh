#!/usr/bin/env bash
set -euo pipefail

# Bootstrap pre-commit hooks idempotently
if ! command -v pre-commit &> /dev/null; then
  echo "pre-commit not found, installing..."
  pip install pre-commit
fi
pre-commit install
pre-commit autoupdate
pre-commit run --all-files || true
