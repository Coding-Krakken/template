
# 🧑‍💻 Copilot Instructions for VSMobe

## Architecture & Process
- **Hybrid Workflow**: All work follows a process graph (`.process/graph.yaml`) with nodes (activity, decision, gate, recalibrate). Gates require machine-readable evidence before advancing.
- **Artifacts**: Use templates in `template/artifacts/` for ADRs, RFCs, gates, threat models, runbooks, and postmortems. Every change should link to an artifact.
- **Recalibration**: Triggered quarterly or after incidents (see `runbooks/calibration.md`). Update graph, policies, and document with ADRs.
- **Mobile App**: React Native, entry at `apps/mobile/src/app.tsx`. Components in `components/`, navigation in `navigation/`, screens in `screens/`. Monaco Editor integrated via `EditorWebView.tsx`.

## Dual Root Guidance
This repository has two project roots:
- The **application root** (current working directory) is for the main product code and development.
- The **template root** (`template/`) contains the Universal Hybrid Process Template and all auxiliary files/artifacts for process enforcement, traceability, and evidence.

Copilot must always distinguish which root a file or artifact belongs to. Application code, features, and product development are in the application root. Process, workflow, gates, artifacts, and compliance files are in the template root. All instructions, prompts, and automation should explicitly reference the correct root for each file or artifact.

## Developer Workflows
- **Build**: Use `pnpm install` in root and app folders. Mobile app builds via standard React Native commands.
- **Test**: Achieve ≥99% pass, ≥80% coverage, ≥70% mutation. Mutation testing: `mutmut run` (Linux/macOS) or `python ci/check_mutation.py` (Windows). Edit `ci/check_mutation.py` for source/test modules.
- **CI/CD**: `.github/workflows/validate.yml` enforces gates, evidence, and compliance on PRs. Scripts in `ci/` validate graph, gates, and render diagrams.

## Conventions & Patterns
- **Evidence-Driven Gates**: Never advance past a gate without required evidence (tests, SLOs, SARIF, SBOM, perf, privacy, compliance).
- **Traceability**: All decisions and changes must reference an ADR, RFC, or experiment artifact.
- **Naming**: Follow descriptive, pattern-based naming in `apps/mobile/src/components/` and `template/artifacts/`.
- **AI-Native**: Copilot should propose changes, write tests, enforce gates, and generate missing evidence/artifacts.

## Integration & Communication
- **External**: Monaco Editor (webview), Mutmut/MutPy, pnpm, GitHub Actions.
- **Cross-Component**: Mobile modules communicate via `fileops/`, `git/`, `transport/` boundaries.
- **Process Enforcement**: All gates and evidence checks are automated in CI. Policies in `.process/policies/` (Rego).

## Copilot Operating Model
1. **Perceive**: Load `.process/graph.yaml`, recent ADRs/RFCs, open PR diffs, CI results, SLOs.
2. **Plan**: Map user request to graph node; check prerequisites.
3. **Act**: Generate/edit artifacts from templates; write code/tests; suggest rollout plans.
4. **Check**: Run gate/policy scripts; summarize pass/fail and missing evidence.
5. **Learn**: Capture postmortems/recalibration; update graph/policies.

## Examples
- **Add a component**: Place in `apps/mobile/src/components/`, update navigation/screens.
- **Document a decision**: Use `template/artifacts/adr/ADR_TEMPLATE.md`.
- **Enforce a gate**: Update `.process/graph.yaml`, ensure required evidence is present, validate via CI.

---
For missing conventions, review `template/README.md`, `template/docs/architecture/README.md`, `template/docs/vision.md`, and `.github/workflows/validate.yml`. If any section is unclear, request feedback or clarification.
