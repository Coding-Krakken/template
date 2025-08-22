// Real OpenTelemetry SDK setup for Node.js
import { context, Span, trace, Tracer } from '@opentelemetry/api';
import { registerInstrumentations } from '@opentelemetry/instrumentation';
import { resourceFromAttributes } from '@opentelemetry/resources';
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

let provider: NodeTracerProvider | undefined;

export function initOtel(serviceName = 'template-service'): void {
  provider = new NodeTracerProvider({
    resource: resourceFromAttributes({
      [SemanticResourceAttributes.SERVICE_NAME]: serviceName,
    }),
  });
  provider.register();
  registerInstrumentations({
    instrumentations: [], // Add desired instrumentations here
  });
}

export function getTracer(): Tracer {
  return trace.getTracer('template-service');
}

export function startSpan(name: string): Span {
  return getTracer().startSpan(name);
}

export function withSpan<T>(name: string, fn: () => T): T {
  const span = startSpan(name);
  try {
    return context.with(trace.setSpan(context.active(), span), fn);
  } finally {
    span.end();
  }
}
