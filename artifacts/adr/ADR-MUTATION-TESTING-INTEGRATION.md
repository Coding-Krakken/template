# Mutation Testing Gate Implementation

## Overview

This document describes the implementation of mutation testing as part of the CI/CD quality gates, as specified in the vision.md document. Mutation testing is now integrated as a mandatory gate check to ensure code quality meets the target of ≥70% mutation score.

## Implementation Details

### New CI Script: `ci/check_mutation.py`

- **Purpose**: Runs mutation testing using `mutmut` and validates the mutation score against quality targets
- **Target Score**: 70% (configurable via `--target-score` parameter)
- **Evidence Output**: Machine-readable JSON report in `artifacts/evidence/mutation_score.json`
- **Integration**: Added to GitHub Actions workflow in `.github/workflows/validate.yml`

### Process Graph Updates

Updated `.process/graph.yaml` to include mutation testing requirements in the G-verify gate:

```yaml
- id: G-verify
  kind: gate
  description: >
    Verification gate. Requires unit/integration/end‑to‑end tests to pass,
    security scans to show zero critical vulnerabilities, mutation testing
    score to meet quality targets (≥70%), and performance measurements to 
    meet non‑functional targets. Failure leads to a fix iteration.
  requires:
    - metric: test.pass_rate >= 0.99
    - metric: security.critical_vulns == 0
    - metric: mutation.score >= 0.7
    - metric: performance.p95_latency_ms <= target
    - artifact: artifacts/evidence/mutation_score.json
```

### NFR Requirements Update

Added mutation testing target to `requirements/nfr.yml`:

```yaml
maintainability:
  code_coverage_min: 0.8              # minimum acceptable code coverage
  mutation_score_min: 0.7             # minimum acceptable mutation testing score
  dependency_update_interval_days: 30  # frequency of dependency updates
  documentation_completeness: 1.0     # 1.0 = complete
```

## Usage

### Manual Execution

```bash
# Run with default 70% target
python3 ci/check_mutation.py

# Run with custom target
python3 ci/check_mutation.py --target-score 0.8

# Specify custom source directory and test command
python3 ci/check_mutation.py --source-dir src --test-cmd "pytest tests/"
```

### CI Integration

The mutation testing check is automatically executed as part of the CI pipeline:

1. GitHub Actions workflow installs dependencies including `mutmut`
2. Validates process graph structure
3. Checks gate artifacts
4. **Runs mutation testing** - fails build if score < 70%
5. Renders process diagrams

### Evidence Format

The script generates machine-readable evidence in JSON format:

```json
{
  "timestamp": "2025-08-21T17:07:45.920063",
  "tool": "mutmut",
  "target_score": 0.7,
  "actual_score": 0.7428571428571429,
  "passed": true,
  "total_mutations": 35,
  "killed_mutations": 26,
  "survived_mutations": 9,
  "skipped_mutations": 0,
  "timeout_mutations": 0,
  "evidence_level": "HIGH"
}
```

## Configuration

### Mutation Testing Tool: mutmut

- **Configuration**: `pyproject.toml` with `[tool.mutmut]` section
- **Paths**: Configurable via `paths_to_mutate` setting
- **Test Runner**: Configurable via `runner` setting

### Example Structure for New Projects

When implementing mutation testing in a new project:

1. Create `src/` directory for source code
2. Create `tests/` directory for test files  
3. Ensure test coverage is comprehensive
4. Configure `pyproject.toml` with appropriate paths
5. Run `python3 ci/check_mutation.py` to validate

## Quality Targets Alignment

This implementation aligns with the vision.md quality targets:

- **Target**: Mutation score ≥ 70%
- **Quality Gate**: Hard requirement before release
- **Evidence-Driven**: Machine-readable artifacts required
- **CI Integration**: Automated enforcement in pipeline

## Benefits

1. **Higher Code Quality**: Detects weak tests that don't validate actual behavior
2. **Test Effectiveness**: Measures how well tests catch bugs
3. **Automated Enforcement**: Prevents regression in test quality
4. **Alignment with Vision**: Supports 70% defect escape rate reduction goal
5. **Process-as-Code**: Configuration and thresholds in version control

## Next Steps

1. Integrate with additional mutation testing tools (e.g., cosmic-ray)
2. Add mutation testing coverage for different languages
3. Implement mutation testing reporting dashboard
4. Create mutation testing best practices guide