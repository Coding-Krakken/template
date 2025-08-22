# scripts/overlay/ci/

Canonical CI scripts for the template repository.

## Files
- `config_eval.ts`: Exports config env vars for CI scripts.
- `coverage.sh`: Coverage gate for supported languages.
- `docs_check.sh`: Docs/ADR verification gate.
- `semgrep.yml`: Semgrep config for security and quality scanning.

### Usage
- Overlays are applied to the main `ci/` directory via `apply_overlay.sh`.
- Update these files to change canonical CI behavior.
