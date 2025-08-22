# Guardrail Checklist

- No secrets in code or config (scan with Semgrep, gitleaks)
- API stability enforced (contract tests)
- Coverage threshold met (CI gate)
- ADRs updated for architecture changes
- Accessibility and i18n if UI
- All endpoints expose health, readiness, and metrics
- Feature flags and observability present in all services
