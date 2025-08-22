import http from 'http';
import { describe, expect, it } from 'vitest';
import { handler } from '../helpers/service-handler.js';

function makeRequest(path: string): Promise<{ status: number; body: any }> {
  return new Promise((resolve) => {
    const server = http.createServer(handler);
    server.listen(0, () => {
      const port = (server.address() as any).port;
      http.get({ port, path }, (res) => {
        let data = '';
        res.on('data', (chunk) => (data += chunk));
        res.on('end', () => {
          server.close();
          resolve({ status: res.statusCode || 0, body: JSON.parse(data) });
        });
      });
    });
  });
}

describe('Contract: Health endpoint', () => {
  it('Given the service is running, When I call /health, Then I get status ok', async () => {
    const res = await makeRequest('/health');
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ status: 'ok' });
  });
});
