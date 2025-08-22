import express from 'express';
import request from 'supertest';
import { describe, expect, it } from 'vitest'; // ESM import, Vitest must be run with node --loader

const app = express();
app.get('/health', (req, res) => res.json({ status: 'ok' }));

describe('GET /health', () => {
  it('should return status ok', async () => {
    const res = await request(app).get('/health');
    expect(res.body).toEqual({ status: 'ok' });
  });
});
