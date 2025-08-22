# packages/feature-flags/

Feature flag context and evaluation logic for the template repository.

## Files
- `index.ts`: Implements feature flag definitions, context-aware evaluation, variants, and change listeners.

## Features
- Supports runtime toggling of features.
- Enables gradual rollout and context-based activation.
- Used by applications and services to control feature exposure.

### Usage
- Import and use `FeatureFlags` in services to enable/disable features dynamically.
- Extend flag definitions and rules as needed.
