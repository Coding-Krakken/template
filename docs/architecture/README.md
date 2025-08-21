# 🚀 Hybrid Workflow Template  
*A Universal, Process-as-Code Framework for AI-Accelerated Engineering*

![workflow](https://img.shields.io/badge/process-as--code-blue?style=flat-square)
![ci](https://github.com/Coding-Krakken/MaintAInPro/actions/workflows/validate.yml/badge.svg)

---

## 🌟 Overview

This repository implements a **hybrid workflow system**:  

It is designed to be **language-agnostic, project-agnostic, and AI-native** — enabling GitHub Copilot and other AI agents to dramatically improve **quality, speed, and reliability**.


## 🧭 Vision

> “A process that is as deterministic as a compiler, as adaptive as a feedback loop.”

- **Process as Code**: Workflows live in versioned YAML + policies, not tribal knowledge.  
- **Evidence-Driven Quality**: Gates require machine-readable artifacts, tests, and metrics.  
- **AI-Accelerated**: Copilot creates artifacts, writes tests, enforces gates, and proposes rollouts.  
- **End-to-End Traceability**: Every change is linked to an ADR, RFC, or experiment.


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

* ✅ Tests ≥ 99% pass, coverage ≥ 80%, mutation ≥ 70% (using [Mutmut](https://mutmut.readthedocs.io/en/latest/))
* ✅ 0 critical vulnerabilities (SAST/DAST, deps)
* ✅ Performance budgets respected (p95 latency, throughput)
* ✅ Privacy & compliance sign-offs complete

### Mutation Testing (Mutmut)

Mutation testing is enforced via [Mutmut](https://mutmut.readthedocs.io/en/latest/) (Linux/macOS only).

> **Note:** Mutmut is not compatible with Windows due to its dependency on the `resource` module. For Windows, use [MutPy](https://mutpy.readthedocs.io/en/latest/) as an alternative.

#### Linux/macOS:
```bash
# Run mutation tests
mutmut run
# Show results
mutmut results
# Required: mutation score ≥ 70%
```

#### Windows:
```bash
# Run mutation tests via CI script
python ci/check_mutation.py
# Required: mutation score ≥ 70%
```

Edit `ci/check_mutation.py` to set your source and test modules. The script will enforce the mutation score threshold for gate passage.

Evidence of mutation score must be included for gate passage.

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

* [ ] Integrate mutation testing into CI — Next step: add mutation testing to CI scripts and document evidence requirements
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

