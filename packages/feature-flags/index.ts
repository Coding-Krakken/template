// Canonical Feature-Flag Facade for Template Repo
// Simple feature flag system for template

export type FeatureFlagContext = Record<string, any>;

const flags: Record<string, boolean> = {
  enableMetrics: true,
  experimentalFeature: false,
};

export function isEnabled(flag: string, context?: FeatureFlagContext): boolean {
  // Basic provider: returns flag value or false if not set
  return !!flags[flag];
}

export function setFeatureFlag(flag: string, value: boolean): void {
  flags[flag] = value;
}
