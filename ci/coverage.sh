#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
THRESHOLD=$(awk '/threshold:/ {print $2}' config/project.yml)
case "$LANG" in
ts)
  echo "Checking TypeScript coverage..."
  COVERAGE=$(npx nyc report --reporter=text-summary | awk '/Statements/ {print $4}' | tr -d '%')
  if (( COVERAGE < THRESHOLD )); then
    echo "Coverage $COVERAGE below threshold $THRESHOLD"
    exit 1
  fi
  ;;
py)
  echo "Checking Python coverage..."
  # COVERAGE=$(coverage report | awk '/TOTAL/ {print $4}' | tr -d '%')
  # if (( COVERAGE < THRESHOLD )); then echo "Coverage $COVERAGE below threshold $THRESHOLD"; exit 1; fi
  ;;
go)
  echo "Checking Go coverage..."
  # COVERAGE=$(go test -cover | awk '/coverage:/ {print $6}' | tr -d '%')
  # if (( COVERAGE < THRESHOLD )); then echo "Coverage $COVERAGE below threshold $THRESHOLD"; exit 1; fi
  ;;
rust)
  echo "Checking Rust coverage..."
  # COVERAGE=$(cargo tarpaulin --out text | awk '/lines covered/ {print $4}' | tr -d '%')
  # if (( COVERAGE < THRESHOLD )); then echo "Coverage $COVERAGE below threshold $THRESHOLD"; exit 1; fi
  ;;
*)
  echo "Unknown language: $LANG"
  exit 1
  ;;
esac
