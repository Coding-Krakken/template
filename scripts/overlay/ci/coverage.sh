
#!/usr/bin/env bash
set -euo pipefail

# Canonical Coverage Gate for Template Repo
# Sources config envs from config_eval.ts

eval "$(node ci/config_eval.ts | awk -F= '{print \"export \" $1 \"=\\\"\" $2 \"\\\"\"}')"

echo "COVERAGE_THRESHOLD is $TPL_COVERAGE_THRESHOLD"

LANG="${TPL_LANGUAGE:-ts}"

# Coverage parser stubs for supported languages
case "$LANG" in
	ts)
		# TypeScript: expects coverage report at coverage/coverage-summary.json
		if [ -f coverage/coverage-summary.json ]; then
			COVERAGE=$(jq '.total.lines.pct' coverage/coverage-summary.json)
			echo "Detected TypeScript coverage: $COVERAGE%"
		else
			echo "No TypeScript coverage report found."
			COVERAGE=0
		fi
		;;
	py)
		# Python: expects coverage report at coverage.xml
		if [ -f coverage.xml ]; then
			COVERAGE=$(grep -o 'line-rate="[^\"]*"' coverage.xml | head -1 | cut -d'"' -f2)
			COVERAGE=$(awk "BEGIN {print $COVERAGE * 100}")
			echo "Detected Python coverage: $COVERAGE%"
		else
			echo "No Python coverage report found."
			COVERAGE=0
		fi
		;;
	go)
		# Go: expects coverage report at coverage.out
		if [ -f coverage.out ]; then
			COVERAGE=$(go tool cover -func=coverage.out | awk '/total:/ {print $3}' | sed 's/%//')
			echo "Detected Go coverage: $COVERAGE%"
		else
			echo "No Go coverage report found."
			COVERAGE=0
		fi
		;;
	rust)
		# Rust: expects coverage report at target/coverage/lcov.info
		if [ -f target/coverage/lcov.info ]; then
			COVERAGE=$(awk -F: '/LF:/ {lf+=$2} /LH:/ {lh+=$2} END {if (lf>0) print lh/lf*100; else print 0}' target/coverage/lcov.info)
			echo "Detected Rust coverage: $COVERAGE%"
		else
			echo "No Rust coverage report found."
			COVERAGE=0
		fi
		;;
	*)
		echo "Unsupported language for coverage parsing: $LANG"
		COVERAGE=0
		;;
esac

THRESHOLD="${TPL_COVERAGE_THRESHOLD:-85}"

if [ "$(awk "BEGIN {print ($COVERAGE >= $THRESHOLD)}")" -eq 1 ]; then
	echo "Coverage check PASSED ($COVERAGE% >= $THRESHOLD%)"
	exit 0
else
	echo "Coverage check FAILED ($COVERAGE% < $THRESHOLD%)"
	exit 1
fi
