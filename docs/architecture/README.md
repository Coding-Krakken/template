# 🚀 Hybrid Workflow Template  
*A Universal, Process-as-Code Framework for AI-Accelerated Engineering*

![workflow](https://img.shields.io/badge/process-as--code-blue?style=flat-square)
![ci](https://github.com/Coding-Krakken/MaintAInPro/actions/workflows/validate.yml/badge.svg)

---

## 🌟 Overview

This repository implements a **hybrid workflow system**:  
- A **decision graph** (`.process/graph.yaml`) encoding the entire software lifecycle.  
- **Hard gates** (evidence-driven checkpoints) ensuring quality and compliance.  
- **Recalibration loops** that keep the process adaptive to real-world change.  
- **Artifact templates** (ADR, RFC, Threat Model, Run Plan, Postmortem) for every key deliverable.  
- **CI/CD scripts and policies** that automatically validate compliance.  

It is designed to be **language-agnostic, project-agnostic, and AI-native** — enabling GitHub Copilot and other AI agents to dramatically improve **quality, speed, and reliability**.

---

## 🧭 Vision

> “A process that is as deterministic as a compiler, as adaptive as a feedback loop.”

- **Process as Code**: Workflows live in versioned YAML + policies, not tribal knowledge.  
- **Evidence-Driven Quality**: Gates require machine-readable artifacts, tests, and metrics.  
- **Adaptive Hybrid Flow**: Hard stops where safety demands it, recalibration where agility is needed.  
- **AI-Accelerated**: Copilot creates artifacts, writes tests, enforces gates, and proposes rollouts.  
- **End-to-End Traceability**: Every change is linked to an ADR, RFC, or experiment.

---

## 📊 Process Graph

The system’s backbone is `.process/graph.yaml`. It encodes activities, decisions, and gates.

```mermaid
flowchart TD
  A["A: Discovery"] --> D1["D-arch: Architecture decision"]
  D1 -->|Choose option| G1["G-design: Design Gate"]
  G1 --> B["B: Build & Implement"]
  B --> G2["G-verify: Verification Gate"]
  G2 --> E["E: Experiment / Rollout"]
  E --> R["Release"]
  R --> O["Operate"]
  O --> D2["D-calibrate: Recalibration"]
  D2 -->|Loop back| A
````

---

## 📂 Repository Structure

<details>
<summary>Click to expand</summary>

```
├── .process/
│   ├── graph.yaml              # Workflow definition
│   ├── schema/                 # Node schemas
│   └── policies/               # Gate + recalibration rules
├── artifacts/
│   ├── adr/ADR_TEMPLATE.md     # Architecture Decision Record
│   ├── rfc/RFC_TEMPLATE.md     # Request for Comments
│   ├── gate/GATE_TEMPLATE.md   # Gate checklist
│   ├── run/RUN_TEMPLATE.md     # Experiment/run plan
│   ├── threat/THREAT_TEMPLATE.md
│   └── postmortem/POSTMORTEM_TEMPLATE.md
├── requirements/
│   ├── frd.md                  # Functional requirements
│   ├── nfr.yml                 # Non-functional requirements
│   ├── privacy.yml             # Privacy requirements
│   └── compliance.yml          # Compliance requirements
├── runbooks/                   # On-call, rollback, release, calibration
├── ci/                         # Validation scripts
│   ├── validate_graph.py
│   ├── check_gates.py
│   └── render_diagrams.py
├── docs/                       # Vision, discovery, design decisions
└── .github/workflows/validate.yml
```

</details>

---

## 📜 Artifacts

| Artifact       | Purpose                             | Template                                      |
| -------------- | ----------------------------------- | --------------------------------------------- |
| ADR            | Architecture decision w/ trade-offs | `artifacts/adr/ADR_TEMPLATE.md`               |
| RFC            | Feature/system proposal             | `artifacts/rfc/RFC_TEMPLATE.md`               |
| Gate           | Hard checkpoint w/ evidence list    | `artifacts/gate/GATE_TEMPLATE.md`             |
| Run/Experiment | Hypothesis, guardrails, rollout     | `artifacts/run/RUN_TEMPLATE.md`               |
| Threat Model   | STRIDE, mitigations, risks          | `artifacts/threat/THREAT_TEMPLATE.md`         |
| Postmortem     | Incident analysis & lessons         | `artifacts/postmortem/POSTMORTEM_TEMPLATE.md` |

---

## ✅ Gates & Evidence

Gates are enforced through **policies** and **CI scripts**:

* `ci/validate_graph.py` → ensures the process graph is valid.
* `ci/check_gates.py` → verifies required artifacts exist.
* `ci/render_diagrams.py` → generates diagrams from YAML.
* Policies (`.process/policies/*.rego`) → enforce quality/security thresholds.

**Default requirements include**:

* ✅ Tests ≥ 99% pass, coverage ≥ 80%, mutation ≥ 70%
* ✅ 0 critical vulnerabilities (SAST/DAST, deps)
* ✅ Performance budgets respected (p95 latency, throughput)
* ✅ Privacy & compliance sign-offs complete

---

## 🔄 Recalibration

Regular **recalibration sessions** (guided by `runbooks/calibration.md`) ensure the process adapts:

* Triggered **quarterly** or after incidents.
* Review SLOs, postmortems, and NFR budgets.
* Update `.process/graph.yaml` and policies.
* Document changes with ADRs.

---

## 🤖 Copilot Workflow

Copilot should operate as a **process navigator + enforcer**:

1. **Map user request → graph node**
2. **Check prerequisites & gates**
3. **Create/update artifacts from templates**
4. **Run validation scripts & report evidence gaps**
5. **Guide recalibration if metrics/conditions require it**

> ⚠️ **Golden Rule**: Never advance past a gate without required evidence.

---

## 📈 Roadmap

* [ ] Integrate mutation testing into CI
* [ ] Automerge PRs that pass all gates
* [ ] Add cost/performance budgets enforcement
* [ ] Enable progressive delivery guardrails (flags, canaries)
* [ ] Expand recalibration automation (metrics-driven)

---

## 📚 Resources

* **Runbooks** → `runbooks/`
* **Vision doc** → `docs/vision.md`
* **Templates** → `artifacts/`
* **Process graph** → `.process/graph.yaml`

---

## 💡 Quickstart

```bash
# Validate process graph
python3 ci/validate_graph.py

# Check all gates
python3 ci/check_gates.py

# Render process diagram
python3 ci/render_diagrams.py --output flowchart.mmd
```

---

## 🛡️ Governance

* All process changes must be proposed via **ADR** and PR.
* Waivers are explicit, time-boxed, and documented.
* Recalibration cadence: **quarterly + postmortem triggered**.
* No skipping gates, ever.

---

## 📜 License

[MIT](LICENSE)

---

