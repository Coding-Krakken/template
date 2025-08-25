# Traceability Matrix

This matrix links all critical features, requirements, ADRs, RFCs, gate evidence, and test coverage for the project. Update as new features and decisions are added.

| Feature/Module                | Requirement(s)         | ADR/RFC                        | Gate Evidence                        | Test Coverage |
|-------------------------------|------------------------|-------------------------------|--------------------------------------|--------------|
| Monaco Editor Integration     | FRD, NFR, Privacy      | ADR-20250825-monaco-webview.md | EditorWebView.tsx, privacy sign-off  | Yes          |
| Explorer Component            | FRD, NFR               | ADR-0001.md, RFC-0001.md       | Explorer.tsx                         | Yes          |
| Editor Component              | FRD, NFR               | ADR-0001.md, RFC-0001.md       | Editor.tsx                           | Yes          |
| Terminal Component            | FRD, NFR               | ADR-0001.md, RFC-0001.md       | Terminal.tsx                         | Yes          |
| Mutation Testing in CI        | NFR, Security          | -                             | check_mutation.py, gate template     | Yes          |
| Progressive Delivery (Canary) | NFR, Reliability       | -                             | rollout/PLAN-0001.md                 | Planned      |
| Recalibration Automation      | NFR, Ops               | -                             | runbooks/calibration.md              | Planned      |

*Update this file as features, requirements, and evidence evolve. Link to source files, ADRs, RFCs, and gate artifacts as needed.*
