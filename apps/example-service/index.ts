import express from 'express';
// Use dynamic path resolution for subdirectory support
import path from 'path';
import { fileURLToPath } from 'url';
import { setupOtel } from './otel.js';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const featureFlagsPath = path.resolve(
  __dirname,
  '../../packages/feature-flags/index.js',
);
// eslint-disable-next-line @typescript-eslint/no-var-requires
const { FeatureFlags } = require(featureFlagsPath);

const app = express();
const flags = new FeatureFlags();
setupOtel(app); // OpenTelemetry wiring stub

app.get('/health', (req, res) => res.json({ status: 'ok' }));
app.get('/ready', (req, res) => res.json({ ready: true }));
app.get('/metrics', (req, res) => res.send('# Metrics stub'));

app.listen(3000, () => console.log('Example service running on port 3000'));
