#!/usr/bin/env bash
set -euo pipefail

# Canonical Docs Verify Gate for Template Repo
# Sources config envs from config_eval.ts

eval "$(node ci/config_eval.ts | awk -F= '{print \"export \" $1 \"=\\\"\" $2 \"\\\"\"}')"

echo "DOCS_REQUIRE_UPDATE_ON_API_CHANGE is $TPL_DOCS_REQUIRE_UPDATE_ON_API_CHANGE"

if [ "${TPL_DOCS_REQUIRE_UPDATE_ON_API_CHANGE}" = "true" ]; then
	# Detect API-surface changes (stub: allowlist/denylist)
	# Example: git diff --name-only $BASE_SHA $HEAD_SHA
	# API files: src/**, packages/**, services/**
	# Docs/ADR files: docs/**, artifacts/adr/**
	# If any API file changed and no docs/ADR file changed, fail.

	# TODO: Implement logic using git diff, allowlist/denylist.
	echo "API-surface change detection and docs/ADR update check not implemented (template stub)."
	# exit 1 if check fails
else
	echo "Docs update on API change not required by config."
fi
