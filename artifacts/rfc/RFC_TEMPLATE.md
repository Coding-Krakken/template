---
# Front‑matter
id: rfc-XXXX
title: "Feature or system proposal"
author: your.name@example.com
date: YYYY-MM-DD
status: draft  # draft | review | accepted | rejected | superseded
tags: [architecture, design]
---

# Summary

Provide a concise overview of the proposed feature or system change, including the
problem it solves and the high‑level approach.

# Motivation

Explain why this change is necessary or desirable.  Outline current pain points,
opportunities, and the expected impact on users or the business.

# Detailed Design

Describe the proposed solution in detail.  Include architecture diagrams,
API/interface definitions, state transitions, data models, and any interactions
with existing systems.  You can link diagrams generated from the process
graph or embed Mermaid/PlantUML diagrams.

# Alternatives Considered

List and briefly discuss alternative solutions that were considered, including
their pros and cons and reasons for rejection.

# Security and Privacy Considerations

Identify potential security vulnerabilities and privacy concerns.  Reference
threat models or STRIDE analyses where appropriate.

# Non‑Functional Requirements (NFRs)

Explain how the proposed design meets performance, reliability, scalability,
accessibility, and other non‑functional requirements.  Link to `requirements/nfr.yml`.

# Rollout Plan

Outline how the feature will be delivered.  Discuss phased rollouts, feature
flags, canary deployments, and migration strategies.  Include fallback or
rollback procedures in case of issues.

# Open Questions

List unresolved issues or areas where further investigation is required.

# References

Link to supporting documents, tickets, or previous RFCs and ADRs.