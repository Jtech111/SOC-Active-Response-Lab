# SOC Active Response Lab

## Tier 1/2 SOC Operations, Detection Engineering & Incident Response

This repository documents a hands-on Security Operations Center lab focused on the complete alert lifecycle:

**Detect → Triage → Investigate → Enrich → Scope → Classify → Escalate → Contain → Remediate → Validate → Document**

The lab combines SIEM monitoring, detection engineering, Linux and Windows investigation, network telemetry, IOC enrichment, automation, active response, and defensive hardening.

---

## SOC Mission

The objective of this lab is not simply to generate security alerts.

The objective is to demonstrate how a SOC analyst takes an alert from initial detection through investigation, response, validation, and documentation.

The lab therefore emphasizes both:

- Technical detection capability
- Analyst decision-making and operational discipline

---

## SOC Environment

| Capability | Technology |
|---|---|
| SIEM / Detection | Wazuh |
| Cloud SIEM | Splunk Cloud |
| Cloud Security Analytics | Microsoft Sentinel |
| Detection Logic | Wazuh Rules, SPL, KQL |
| Endpoint Investigation | Linux / Windows telemetry |
| Network Investigation | Network logs and packet analysis |
| Threat Intelligence | IOC enrichment |
| Automation | Python / REST APIs |
| Active Response | fail2ban / UFW / endpoint controls |
| Framework | MITRE ATT&CK |

---

## Analyst Workflow

```text
Alert
  ↓
Validate Detection
  ↓
Initial Triage
  ↓
Identify Source / Target
  ↓
Investigate Evidence
  ↓
Determine Scope
  ↓
Classify
  ↓
Escalate if Required
  ↓
Contain
  ↓
Remediate
  ↓
Validate
  ↓
Document / Close
```




## Incident Investigations


