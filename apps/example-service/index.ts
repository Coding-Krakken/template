import express from 'express';
import { FeatureFlags } from '../../packages/feature-flags/index.js';
import { setupOtel } from './otel.js';

const app = express();
const flags = new FeatureFlags();
setupOtel(app); // OpenTelemetry wiring stub

app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.get('/ready', (req, res) => res.json({ ready: true }));
app.get('/metrics', (req, res) => res.send('# Metrics stub'));

app.listen(3000, () => console.log('Example service running on port 3000'));
