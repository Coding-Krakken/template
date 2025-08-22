# apps/

This directory contains application entrypoints for the template repository. Each subdirectory represents a standalone application or service, typically exposing HTTP endpoints and integrating shared libraries.

## Subdirectories
- `example-service/`: Canonical Express.js service demonstrating health, readiness, and metrics endpoints, feature flag integration, and OpenTelemetry wiring.

### Usage
- Add new applications as subdirectories.
- Use shared packages for feature flags and observability.
- Entry points should follow the template's guardrails for coverage, security, and documentation.
