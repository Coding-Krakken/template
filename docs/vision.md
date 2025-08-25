# Vision: Hybrid Process-as-Code System for Elite, AI-Accelerated Engineering

## Mission

Build a **universal, language-agnostic, process-as-code system** that Copilot (and other LLMs) can *operate, enforce, and learn from* to produce **consistently higher-quality software, faster**, with provable safety, security, and reliability.

## North-Star Outcomes

* **Quality:** Defect escape rate ↓ 70%; security criticals at release = 0.
* **Speed:** Lead time for changes ↓ 50%; review turnaround ≤ 24h p95.
* **Reliability:** SLOs met ≥ 99.9% with enforced error budgets.
* **Traceability:** 100% of code changes linked to ADR/RFC and tests.
* **Confidence:** Progressive delivery with automatic rollback yields <1% bad-deploy minutes per quarter.

## Scope & Boundaries

* **In scope:** Any project (app, service, library, infra, data/ML) in any language. Full lifecycle: discovery → design → build → verify → experiment → release → operate → learn.
* **Out of scope:** Bypassing gates “for speed”; untracked changes; release without evidence.

## Design Principles

* **Process as Code:** The workflow is a **decision graph** (`.process/graph.yaml`), not tribal knowledge.
* **Evidence-Driven:** Gates pass only with **machine-readable evidence** (tests, SLOs, SARIF, SBOM, perf).
* **Adaptive, not rigid:** **Hybrid** model: hard gates + scheduled **recalibration loops** (policy updates via PRs).
* **Human-in-the-Loop by default:** Copilot proposes, **gates and reviews** decide.
* **Security & Privacy by design:** Threat modeling, dependency hygiene, provenance, and privacy checks are first-class.

## Core Capabilities

### 1) Process Graph & Governance

* **Nodes:** `activity`, `decision`, `gate`, `calibrate`.
* **Artifacts:** ADR, RFC, Gate Checklist, Threat Model, Run/Experiment, Postmortem, SBOM, SARIF, Perf report.
* **Policies:** Rego/Python gate checks (security, tests, perf, privacy, compliance).
* **Recalibration:** Time/trigger-based sessions to update graph, thresholds, and templates.

### 2) Evidence & Telemetry Fabric

* **Quality:** Unit/integration/e2e results (JUnit XML), **mutation testing** score, coverage.
* **Security:** SAST/DAST/secret scan (SARIF), **dependency vulns**, signed attestations, SBOM (CycloneDX).
* **Performance & Cost:** p95/p99 latency and throughput JSON; cost per request/build.
* **Reliability:** SLO/error-budget snapshots, incident timelines, MTTR.
* **Product:** A/B results, guardrails (crash rate, latency, churn).

### 3) AI-Native Workbench for Copilot

* **Artifact Synthesis:** Auto-draft ADRs/RFCs/gate docs from context + diffs.
* **Guardrail-Aware Coding:** Proposes code aligned with current **NFR budgets** (perf, memory, cost).
* **Test Intelligence:** Generates **property-based tests**, fuzz targets, and mutation operators.
* **Review Agent:** PR review that cites policy violations with **fix-it patches**.
* **Release Navigator:** Proposes flag ramps, canary cohorts, rollback triggers, and anti-patterns to avoid.

### 4) Toolchain Integration (extensible)

* **IDE:** VS Code / JetBrains Copilot Chat commands bound to graph actions.
* **CI/CD:** GitHub Actions (or equivalent) running `validate_graph.py`, `check_gates.py`, `render_diagrams.py`, scanners, and provenance.
* **Observability:** Pull SLOs & dashboards for gate checks; post results to PRs.
* **Package Supply Chain:** SBOM + provenance attached to artifacts/releases.

## Copilot Operating Model

1. **Perceive:** Load `.process/graph.yaml`, recent ADRs/RFCs, open PR diffs, CI results, SLOs.
2. **Plan:** Map user request → current **node**; determine prerequisites; plan actions.
3. **Act:** Generate/edit artifacts from templates; write code; update tests; suggest flags/rollout plans.
4. **Check:** Run gate/policy scripts; summarize pass/fail with exact missing evidence.
5. **Learn:** Capture postmortems and recalibration updates; adjust next steps accordingly.

**Golden rule:** Copilot **never** advances past a gate without required evidence; if missing, it **generates** the artifact/tests or requests exact inputs.

## End-to-End Workflow (Happy Path)

1. **Vision & Constraints** → ADR/RFC drafted; stakeholders aligned.
2. **Discovery** → risks, compliance scan, initial NFR budgets.
3. **Architecture Decision (D-arch)** → ADR with options, tradeoffs, and **reconsider-if** rules.
4. **Design Gate (G-design)** → threat model, privacy sign-off, NFR budget acceptance.
5. **Build** → code + tests; Copilot enforces patterns (logging, feature flags, metrics).
6. **Verify (G-verify)** → unit/integration/e2e ≥ thresholds; SARIF=0 critical; mutation ≥ target; perf p95 ≤ target.
7. **Experiment** → flag on small cohorts; A/B reads guardrails; propose scale/iterate/kill.
8. **Release** → canary → rolling; error budget guard; automatic rollback plan in place.
9. **Operate** → SLOs, on-call runbooks; production fixes loop to Build/Verify.
10. **Learn** → postmortems & analytics inform recalibration; update graph/policies.

## Quality & Safety Gates (Default Targets)

* **Tests:** pass rate ≥ 99%; coverage ≥ 80%; **mutation score ≥ 70%**.
* **Security:** 0 criticals; no leaked secrets; dependency policy clean.
* **Performance:** service-specific p95 ≤ budget; no unacceptable regressions.
* **Reliability:** SLOs met; error-budget burn rate ≤ threshold at ramp.
* **Docs & Traceability:** ADR or RFC linked to every PR; SBOM & provenance attached.

## Metrics & Objectives (example OKRs)

* **O1 (Quality):** Reduce escaped defects by 70% QoQ.
  **KR:** Mutation score ≥ 70%, SARIF criticals = 0 at release.
* **O2 (Speed):** Cut Change Lead Time by 50%.
  **KR:** p95 review turnaround ≤ 24h; auto-merge for policy-clean PRs.
* **O3 (Reliability):** Meet SLOs ≥ 99.9% with disciplined budgets.
  **KR:** ≤ 1% bad-deploy minutes per quarter; rollback MTTR ≤ 15m.
* **O4 (Adoption):** ≥ 90% of changes reference an ADR/RFC; ≥ 95% gates enforced by CI.
  **KR:** 100% of releases include SBOM + provenance.

## Governance & Change Management

* **Process Changes:** Proposed via ADR + PR modifying `.process/graph.yaml` and policies; require approval from **Process Owners** (RACI).
* **Risk-Based Depth:** Higher risk = deeper gates (security, perf, privacy).
* **Escalation:** If evidence can’t be produced, Copilot blocks, explains why, and offers a minimal path to green.

## Risks & Mitigations

* **Process Drift:** Mitigate with CI gate checks + recalibration cadence.
* **Policy Over-constraint:** Track dev friction; relax rules with data; keep waivers explicit and time-boxed.
* **LLM Hallucinations:** Require artifact + gate evidence; restrict actions to graph; embed deterministic checks.
* **Secret/Data Leakage:** Mandatory secret scanning, redaction, and privacy gates; no training on sensitive data.

## 180-Day Roadmap (example)

* **0–30 days:** Roll out template repo; wire CI checks; pilot one service; adopt ADR template; enable basic security/perf gates.
* **31–90 days:** Add mutation testing, fuzzing; connect SLO/error-budget exports; enable progressive delivery with flags; introduce privacy/compliance gates.
* **91–180 days:** Policy-driven auto-merge for clean PRs; cost/perf budgets; Copilot release navigator; experiment guardrails with automatic decisions; quarterly recalibration discipline.

## What “Great” Looks Like (Qualitative)

* Engineers ship confidently because **gates are automated**, evidence is generated as part of the flow, and rollbacks are boring.
* Copilot acts like a **disciplined Staff Engineer**: it proposes changes, writes tests, anticipates gates, and shows receipts.
* Postmortems **improve the graph**, not just the codebase.
* New projects spin up in minutes with a **ready-to-run** process, policies, and templates.

---

### How Copilot Uses This Vision Day-to-Day

* When asked “add rate limiting,” Copilot:

  1. surfaces the NFR perf/cost budgets;
  2. drafts an ADR with options;
  3. updates code + tests;
  4. runs **G-verify**;
  5. proposes a rollout plan with guardrails;
  6. won’t advance past the gate unless evidence is green.
* When a PR fails a gate, Copilot **pinpoints the missing evidence** and generates the artifact or fix (e.g., adds fuzz tests, improves perf, updates SBOM).

## Editor Integration: Monaco via WebView (Mobile)

To deliver a remote-first mobile VS Code client with full editing capabilities, we will integrate the Monaco Editor using a WebView wrapper. This decision is documented in [ADR-20250825-monaco-webview.md](../artifacts/adr/ADR-20250825-monaco-webview.md) and detailed in the architecture README. It enables feature parity, mobile ergonomics, and future extensibility, while maintaining security and performance standards.

- See: [Architecture README](../docs/architecture/README.md)
- See: [ADR-20250825-monaco-webview.md](../artifacts/adr/ADR-20250825-monaco-webview.md)

