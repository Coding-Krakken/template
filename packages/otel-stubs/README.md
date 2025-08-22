# packages/otel-stubs/

OpenTelemetry SDK setup and tracing utilities for Node.js services.

## Files
- `index.ts`: Provides functions to initialize OpenTelemetry, start spans, and run code within a span context.

## Features
- Enables distributed tracing and metrics collection.
- Integrates with OpenTelemetry API and instrumentation packages.

### Usage
- Call `initOtel()` in service entrypoints to enable tracing.
- Use `startSpan` and `withSpan` for custom instrumentation.
