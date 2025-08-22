// Re-export the canonical HTTP handler for tests
// Use dynamic path resolution for subdirectory support
import path from 'path';
import { fileURLToPath } from 'url';
const __dirname = path.dirname(fileURLToPath(import.meta.url));
// Adjust path for subdirectory context
const handlerPath = path.resolve(
  __dirname,
  '../../services/example-service-ts/index.js',
);
// eslint-disable-next-line @typescript-eslint/no-var-requires
export const handler = require(handlerPath).handler;
