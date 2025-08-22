// Canonical Feature-Flag Facade for Template Repo

export type FeatureFlagContext = Record<string, any>;

export function isEnabled(flag: string, context?: FeatureFlagContext): boolean {
  // No-op provider: always returns false (stub)
  // TODO: Integrate with real feature flag system in downstream projects
  return false;
}

// Example usage:
// if (isEnabled('new-dashboard')) {
//   // ...enable feature...
// }
