// Canonical Example Service for Template Repo (TypeScript)

import http from 'http';
// import { initOtel } from '../../packages/otel-stubs'; // Uncomment to enable OTEL

// initOtel(); // No-op in template

export const handler = (
  req: http.IncomingMessage,
  res: http.ServerResponse,
) => {
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok' }));
  } else if (req.url === '/ready') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ready: true }));
  } else if (req.url === '/metrics') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ metrics: {} })); // Stub metrics
  } else {
    res.writeHead(404);
    res.end();
  }
};

if (require.main === module) {
  const server = http.createServer(handler);
  const PORT = process.env.PORT || 3000;
  server.listen(PORT, () => {
    console.log(`Example service listening on port ${PORT}`);
  });
}
