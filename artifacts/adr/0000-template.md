# ADR-0001: Adopt OpenTelemetry for Observability

## Status

Accepted

## Context

The project requires robust distributed tracing and metrics for all services. Existing logging is insufficient for root cause analysis and performance monitoring.

## Decision

Adopt OpenTelemetry as the standard observability framework for all backend services. Integrate tracing and metrics in the canonical template and enforce usage via CI guardrails.

## Consequences

- Improved visibility into service interactions and performance
- Increased operational overhead for instrumentation
- All new services must implement OpenTelemetry tracing and metrics
