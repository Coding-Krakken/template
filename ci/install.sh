#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
case "$LANG" in
ts)
  echo "Installing Node/TypeScript deps..."
  # npm ci
  ;;
py)
  echo "Installing Python deps..."
  # pip install -r requirements.txt
  ;;
go)
  echo "Installing Go deps..."
  # go mod tidy
  ;;
rust)
  echo "Installing Rust deps..."
  # cargo fetch
  ;;
*)
  echo "Unknown language: $LANG"
  exit 1
  ;;
esac
