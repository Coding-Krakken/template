# ci/

Continuous Integration (CI) scripts for the template repository.

## Files
- `install.sh`: Installs dependencies for supported languages (TypeScript, Python, Go, Rust).
- `lint_type.sh`: Runs linter and type checks for all supported languages.
- `test.sh`: Executes tests for all supported languages.
- `coverage.sh`: Enforces coverage thresholds as defined in `config/project.yml`.
- `release.sh`: Release pipeline stub, including SBOM generation and provenance signing.
- `docs_check.sh`: Verifies documentation and ADR updates on API changes.
- `self_check.sh`: Verifies template integrity by checking required files and paths.

### Usage
- Invoked by GitHub Actions and local development workflows.
- Extend scripts to support additional languages or checks as needed.
