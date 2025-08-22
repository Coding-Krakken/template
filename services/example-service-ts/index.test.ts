// Canonical Unit Tests for Example Service (TypeScript)

import http from 'http';
import { AddressInfo } from 'net';
import { afterAll, beforeAll, describe, expect, test } from 'vitest';
import { handler } from './index';

let server: http.Server | undefined;
let port: number;

beforeAll(async () => {
  server = http.createServer(handler);
  await new Promise<void>((resolve) => {
    server!.listen(0, () => {
      port = (server!.address() as AddressInfo).port;
      resolve();
    });
  });
});

afterAll(async () => {
  if (server) {
    await new Promise<void>((resolve) => server!.close(() => resolve()));
  }
});

function request(path: string): Promise<{ status: number; body: any }> {
  return new Promise((resolve) => {
    http.get({ port, path }, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        resolve({
          status: res.statusCode || 0,
          body: JSON.parse(data || '{}'),
        });
      });
    });
  });
}

describe('Example Service', () => {
  test('/health returns ok', async () => {
    const res = await request('/health');
    expect(res.status).toBe(200);
    expect(res.body.status).toBe('ok');
  });

  test('/ready returns ready', async () => {
    const res = await request('/ready');
    expect(res.status).toBe(200);
    expect(res.body.ready).toBe(true);
  });

  test('/metrics returns metrics', async () => {
    const res = await request('/metrics');
    expect(res.status).toBe(200);
    expect(res.body.metrics).toBeDefined();
  });
});
