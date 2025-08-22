#!/usr/bin/env bash
set -euo pipefail
LANG=${1:-ts}
echo "Release pipeline for $LANG"
# SBOM generation (stub)
echo "Generating SBOM..."
# syft . -o json > sbom.json

# Provenance signing (stub)
echo "Signing provenance..."
# cosign sign --key cosign.key artifact.tar.gz
# slsa provenance generate --artifact artifact.tar.gz --output provenance.json
