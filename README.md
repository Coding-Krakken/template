# Universal Hybrid Process Template

This repository provides a **universal, language‑agnostic process framework** built from the hybrid workflow design discussed previously.  It captures both the formal **gated process** used by elite engineering teams and the **recalibration loops** that allow teams to adapt to new information without derailing a project.

The template is intentionally technology‑neutral—you can drop it into any project (web, mobile, backend, ML, hardware, etc.) and adapt the artifacts to your stack.  All process definitions and evidence are stored as code and checked into version control.  The built‑in scripts and policies enforce the gates in CI/CD and provide hooks for periodic recalibration.

## Contents

```
├── README.md                 # this file
├── .process/                 # core process definition (graph, schemas, policies)
│   ├── graph.yaml            # high‑level process graph
│   ├── schema/               # JSON schemas for nodes/gates/decisions
│   │   ├── node_schema.json
│   │   ├── gate_schema.json
│   │   └── decision_schema.json
│   └── policies/            # policy and gate definitions (Rego)
│       ├── gates.rego
│       └── recalibration.rego
├── artifacts/                # templates for process artifacts
│   ├── adr/ADR_TEMPLATE.md
│   ├── rfc/RFC_TEMPLATE.md
│   ├── gate/GATE_TEMPLATE.md
│   ├── run/RUN_TEMPLATE.md
│   ├── threat/THREAT_TEMPLATE.md
│   └── postmortem/POSTMORTEM_TEMPLATE.md
├── requirements/            # requirement definitions
│   ├── frd.md               # functional requirements
│   ├── nfr.yml              # non‑functional requirements
│   ├── privacy.yml          # privacy & data protection requirements
│   └── compliance.yml       # regulatory/compliance requirements
├── runbooks/                # operational guides
│   ├── oncall.md
│   ├── rollback.md
│   ├── release_steps.md
│   └── calibration.md
├── docs/                    # narrative documentation
│   ├── vision.md
│   ├── discovery.md
│   ├── architecture/README.md
│   ├── decisions/README.md
│   └── ops/README.md
├── ci/                      # helper scripts invoked from CI
│   ├── validate_graph.py
│   ├── check_gates.py
│   └── render_diagrams.py
└── .github/workflows/validate.yml  # example GitHub Action for enforcement
```

## Getting Started

1. **Copy or fork this template** into your new project repository.
2. Fill out the templates in `artifacts/` as you make decisions, write RFCs, create threat models, etc.
3. Modify `graph.yaml` to reflect your actual project’s phases and gates.  The default graph includes a typical discovery→design→build→verify→experiment→release→operate loop with recalibration.
4. Define or update the JSON schemas in `.process/schema/` if you need to extend node/gate properties.
5. Implement your own validation logic or extend the provided scripts in `ci/`.  The supplied `validate_graph.py` script verifies basic graph integrity; `check_gates.py` demonstrates how to enforce gates using artifact existence; `render_diagrams.py` converts the graph to Mermaid for visualization.
6. Integrate the example GitHub Action in `.github/workflows/validate.yml` into your CI pipeline to automatically run the checks on pull requests.
7. Schedule periodic recalibration sessions (e.g., quarterly or at major milestones) where you revisit the process graph and update it based on new information or evolving risk.

## Hybrid Workflow Overview

The hybrid workflow combines **hard gates** with **soft recalibration loops**:

* **Formal Gates** (defined in `.process/policies/gates.rego`) ensure essential evidence exists before progressing (e.g. a threat model must exist before design approval, performance tests must meet targets before release).
* **Recalibration** (defined in `.process/policies/recalibration.rego` and represented as `D‑calibrate` in `graph.yaml`) occurs at configurable intervals or after significant events.  During recalibration, the team (or AI assistant) reviews the current state, evaluates whether assumptions still hold, and updates the process graph or requirements as needed.

The process graph is stored as YAML in `.process/graph.yaml`.  Each node has a kind (`activity`, `decision`, `gate`), input/output artifacts, and next steps defined via conditions.  The nodes reference artifacts stored in `artifacts/` and the requirements defined in `requirements/`.  Gates reference policies in `.process/policies/` and scripts in `ci/` to validate evidence.

## Contributing

Feel free to modify or extend this template for your own purposes.  If you find improvements or additional patterns that could benefit others, please contribute back by opening a pull request in your own copy of the template.