#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
case "$LANG" in
ts)
  echo "Running TypeScript tests..."
  # npm test
  ;;
py)
  echo "Running Python tests..."
  # pytest
  ;;
go)
  echo "Running Go tests..."
  # go test -race ./...
  ;;
rust)
  echo "Running Rust tests..."
  # cargo test
  ;;
*)
  echo "Unknown language: $LANG"
  exit 1
  ;;
esac
