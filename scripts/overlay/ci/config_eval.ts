// Config Toggle Engine (canonical)
// Reads config/project.yml if present (future), else uses hardcoded defaults.
// Exports env vars for CI scripts.

const DEFAULTS = {
  LANGUAGE: 'ts',
  MONOREPO: true,
  PROCESS: 'scrum',
  ENGINEERING: 'tdd,bdd,devops',
  COVERAGE_THRESHOLD: 85,
  SEC_CHECKS: 'codeql,secret-scan,semgrep',
  FEATURE_FLAGS: true,
  OPENTELEMETRY: true,
  DOCS_REQUIRE_UPDATE_ON_API_CHANGE: true,
  PROJECT_NAME: 'template',
};

function parseConfig(): Record<string, any> {
  // Future: parse YAML if config/project.yml exists
  // For now, return hardcoded defaults
  return { ...DEFAULTS };
}

function exportEnvVars(config: Record<string, any>) {
  Object.entries(config).forEach(([key, value]) => {
    const envKey = `TPL_${key.toUpperCase()}`;
    console.log(`${envKey}=${value}`);
  });
}

if (require.main === module) {
  const config = parseConfig();
  exportEnvVars(config);
}
