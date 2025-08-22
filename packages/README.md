# packages/

Shared libraries for the template repository. Each subdirectory contains reusable code for feature flags, observability, and other cross-cutting concerns.

## Subdirectories
- `feature-flags/`: Feature flag context and evaluation logic.
- `otel-stubs/`: OpenTelemetry SDK setup and tracing utilities.

### Usage
- Import shared packages in applications and services.
- Extend packages to add new features or integrations.
