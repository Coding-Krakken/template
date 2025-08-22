#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
case "$LANG" in
ts)
  echo "Linting/Typechecking TypeScript..."
  # npm run lint && npm run typecheck
  ;;
py)
  echo "Linting/Typechecking Python..."
  # ruff check . && mypy .
  ;;
go)
  echo "Linting/Typechecking Go..."
  # golangci-lint run && go vet ./...
  ;;
rust)
  echo "Linting/Typechecking Rust..."
  # cargo clippy -- -D warnings
  ;;
*)
  echo "Unknown language: $LANG"
  exit 1
  ;;
esac
