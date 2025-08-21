---
# Front‑matter
id: adr-XXXX
type: decision
title: "Describe the decision succinctly"
status: proposed  # proposed | accepted | superseded | rejected
date: YYYY-MM-DD
owners: [team-name]
inputs: [rfc-XXXX, req-nfr, risk-R001]
options:
  - name: Option A
    pros: [add bullets]
    cons: [add bullets]
  - name: Option B
    pros: [add bullets]
    cons: [add bullets]
decision: Option A  # the chosen option
justification: >
  Summarize why this option was chosen.  Reference evidence, metrics, or experiments
  that support the choice.
impacts: [service-a, service-b]
related_nodes: [D-arch, G-design]
evidence:
  perf_report: artifacts/perf/benchmark-YYYYMMDD.json
  cost_model: artifacts/cost/cost-model.xlsx
reconsider_if:
  - "error_budget.burn_rate > 1.0 for 7d"
  - "lift < 0.05 after two iterations"
---

## Context

Describe the background, goals, and constraints that led to this decision.  Provide
enough detail so future engineers understand the rationale without having to
reverse engineer it from the codebase.

## Decision

Explain the decision made, why it was selected, and any alternative options that were
explicitly considered and rejected.  Link to supporting documents as needed.

## Consequences

Describe the implications of this decision.  Include both positive outcomes and
trade‑offs.  Note any follow‑up work required to implement the decision.