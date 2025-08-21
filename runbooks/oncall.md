# On‑Call Runbook

This runbook provides instructions for engineers participating in the on‑call
rotation.  Customize to reflect your monitoring tools, escalation policies,
communication channels, and operational procedures.

## Responsibilities

* Monitor alerts and dashboards for assigned services.
* Triage incidents according to severity and impact.
* Coordinate with other teams and stakeholders as needed.
* Keep detailed notes and timelines during incidents.
* Initiate communication with affected users or partners when appropriate.
* File postmortems and track corrective actions after incidents.

## Escalation Policy

1. **Acknowledge**: Respond to the alert within the specified SLA (e.g. 5 minutes).  If unable to respond, the alert escalates to the secondary on‑call.
2. **Assess**: Determine the scope and severity.  Identify if the issue is contained or widespread.
3. **Mitigate**: Apply quick fixes or rollbacks to restore service.  Engage appropriate subject matter experts.
4. **Communicate**: Update status pages, incident channels, and stakeholders regularly.
5. **Resolve**: Once service is restored, verify that all systems are healthy and monitoring is green.
6. **Postmortem**: Create a postmortem document within 48 hours for any Severity 1 or 2 incidents.

## Tooling

List relevant monitoring dashboards, alert systems, and communication tools.  Include URLs and login instructions if needed.