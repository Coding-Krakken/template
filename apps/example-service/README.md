# apps/example-service/

Canonical Express.js application for the template repo.

## Files
- `index.ts`: Main entrypoint. Sets up Express, integrates feature flags, OpenTelemetry stub, and exposes `/health`, `/ready`, `/metrics` endpoints.
- `otel.ts`: Stub for OpenTelemetry SDK wiring. Extend to enable tracing, metrics, and logs.

## Features
- Demonstrates integration of shared packages.
- Follows atomic task and guardrail protocols.
- Serves as a reference for new service implementations.
