## CI Guardrails

- **Coverage Enforcement:** CI will fail if test coverage drops below the threshold set in `config/project.yml` (default: 85%).
- **Docs/ADR Checks:** Any API change in `services/` or `packages/` requires a corresponding update in `docs/` or `artifacts/adr/`.

## Release Pipeline

- **SBOM Generation:** The release script includes a stub for generating a Software Bill of Materials (SBOM) for supply chain security.
- **Provenance Signing:** The release script includes a stub for provenance signing to ensure artifact integrity.

## Contributing & Releasing

- Ensure all code changes meet coverage and documentation requirements.
- Use the release pipeline to generate SBOM and sign provenance before publishing artifacts.
