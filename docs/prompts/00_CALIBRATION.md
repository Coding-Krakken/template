# Calibration Prompt

Copilot: Read and obey the following sources for every atomic task and review:

- docs/vision.md (project vision and goals)
- requirements/frd.md (functional requirements)
- requirements/nfr.yml (non-functional requirements)
- docs/architecture/ (system architecture)
- docs/decisions/ (decision log)
- artifacts/adr/ (architecture decisions)

Respect all toggles in config/project.yml and ensure all guardrails are enforced.
Always check for:

- Coverage, security, and documentation gates
- Feature flag and observability integration
- Accessibility and i18n if UI
