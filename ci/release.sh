#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
echo "Release pipeline for $LANG"
# TODO: Generate SBOM (syft), sign provenance (cosign/SLSA)
