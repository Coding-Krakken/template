// Feature flag context for advanced evaluation
export type FeatureFlagContext = Record<string, any>;

// Flag definition supports variants and context rules
export type FeatureFlagDefinition = {
  enabled: boolean;
  variants?: Record<string, any>;
  rule?: (context: FeatureFlagContext) => boolean;
};

const flags: Record<string, FeatureFlagDefinition> = {
  enableMetrics: { enabled: true },
  experimentalFeature: {
    enabled: false,
    rule: (ctx) => ctx && ctx.userRole === 'admin',
    variants: { rollout: 'gradual' },
  },
};

const listeners: Array<(flag: string, value: boolean) => void> = [];

export function isEnabled(flag: string, context?: FeatureFlagContext): boolean {
  const def = flags[flag];
  if (!def) return false;
  if (def.rule) return def.rule(context ?? {});
  return def.enabled;
}

export function setFeatureFlag(flag: string, value: boolean): void {
  if (!flags[flag]) flags[flag] = { enabled: value };
  else flags[flag].enabled = value;
  listeners.forEach((fn) => fn(flag, value));
}

export function getFlagVariant(flag: string, variant: string): any {
  return flags[flag]?.variants?.[variant];
}

export function onFlagChange(
  listener: (flag: string, value: boolean) => void,
): void {
  listeners.push(listener);
}
