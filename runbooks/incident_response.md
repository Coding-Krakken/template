# Incident Response Plan

This document outlines the steps to follow when responding to security or
privacy incidents.  It is referenced from `requirements/privacy.yml`.

## Objectives

* Protect user data and minimize impact.
* Restore normal service operations quickly.
* Comply with legal and regulatory notification requirements.

## Steps

1. **Detection**: Monitor for indicators of compromise via logs, alerts,
   intrusion detection systems, or external reports.
2. **Assessment**: Immediately involve the security team to assess the
   scope and severity of the incident.  Classify the incident according to
   severity levels.
3. **Containment**: Isolate affected systems to prevent further damage.
4. **Eradication**: Remove malicious artifacts, patch vulnerabilities, and
   harden defenses.
5. **Recovery**: Restore systems to a known good state.  Validate that
   services operate normally and data integrity is maintained.
6. **Notification**: If personal data is involved, notify authorities and
   affected individuals within the time frame specified in `requirements/privacy.yml`.
7. **Post‑Incident Analysis**: Conduct a postmortem to understand root
   causes and update runbooks, policies, and controls.