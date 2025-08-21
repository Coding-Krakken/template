---
id: threat-XXXX
type: threat_model
title: Threat Model for System/Feature
date: YYYY-MM-DD
owners: [security-team]
revision: 1
---

## Overview

Provide a high‑level description of the system or feature being modelled.  Include
context diagrams or data flow diagrams if available.

## STRIDE Analysis

Break down potential threats into the STRIDE categories (Spoofing, Tampering,
Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege).
For each category, list relevant threats, their impact, and proposed mitigations.

## Attack Surfaces

Identify the attack surfaces and entry points an adversary could use.  Discuss
authentication, authorization, input validation, and network exposure.

## Privacy Considerations

Outline how personal data is collected, processed, stored, and transmitted.
Reference `requirements/privacy.yml` and note any data minimization or consent
requirements.

## Mitigations

Describe the security controls, privacy measures, and monitoring strategies that
mitigate the identified threats.  Link to code, configuration, or operational
procedures where applicable.