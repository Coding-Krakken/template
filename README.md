# Subdirectory Integration

This repository can be cloned as a subdirectory (e.g., `Project/this_repository/`) within a larger project. All scripts, overlays, and CI/CD tasks resolve paths relative to their own location, so you can run them from either the subdirectory or the project root.

**Usage:**

- Clone this repository into your project: `git clone <repo> Project/this_repository`
- Run scripts from `this_repository/scripts/` and CI tasks from `this_repository/ci/`
- All overlays and checks will apply to the subdirectory context.

**CI Guardrails**

- Coverage Enforcement: CI will fail if test coverage drops below the threshold set in `config/project.yml` (default: 85%).
- Docs/ADR Checks: Any API change in `services/` or `packages/` requires a corresponding update in `docs/` or `artifacts/adr/`.

**Release Pipeline**

- SBOM Generation: The release script includes a stub for generating a Software Bill of Materials (SBOM) for supply chain security.
- Provenance Signing: The release script includes a stub for provenance signing to ensure artifact integrity.

**Contributing & Releasing**

- Ensure all code changes meet coverage and documentation requirements.
- Use the release pipeline to generate SBOM and sign provenance before publishing artifacts.
