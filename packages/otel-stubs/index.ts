// Canonical OpenTelemetry Stubs for Template Repo
// Basic OpenTelemetry tracer setup for template
// TODO: Integrate with real OpenTelemetry SDK in downstream projects

import { context, Span, trace, Tracer } from '@opentelemetry/api';

export function initOtel(): void {
  // No-op stub for OpenTelemetry initialization
  // Example: Replace with actual OTEL SDK setup
  // e.g., require('@opentelemetry/sdk-node').start();
  // This is a template stub only.
}

export const tracer: Tracer = trace.getTracer('template-service');

export function startSpan(name: string): Span {
  return tracer.startSpan(name);
}

export function withSpan<T>(name: string, fn: () => T): T {
  const span = startSpan(name);
  try {
    return context.with(trace.setSpan(context.active(), span), fn);
  } finally {
    span.end();
  }
}
