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

**Alert → Validate Detection → Initial Triage → Identify Source / Target → Investigate Evidence → Determine Scope → Classify → Escalate if Required → Contain → Remediate → Validate → Document / Close**

---

## Incident Investigations

Documented investigations are maintained in the [SOC Incident Case Register](incidents/README.md).

| ID | Investigation | Status |
|---|---|---|
| INC-001 | SSH Brute Force | Closed |
| INC-002 | Windows Suspicious Execution | Planned |
| INC-003 | Phishing Investigation | Planned |

---

## Triage Framework

SOC investigations use documented standards for severity assessment, escalation, and evidence handling.

- [Severity Matrix](triage/severity-matrix.md)
- [Escalation Matrix](triage/escalation-matrix.md)
- [Evidence Standard](triage/evidence-standard.md)

---

## Detection Engineering

Detection engineering within the lab focuses on:

- SIEM alert development
- Wazuh detection rules
- Splunk SPL queries
- Microsoft Sentinel KQL
- MITRE ATT&CK mapping
- Detection validation
- Alert investigation
- Detection tuning
- False-positive analysis

---

## Incident Response

The lab demonstrates the operational progression from alert to closure:

**Detect → Triage → Investigate → Scope → Classify → Escalate → Contain → Remediate → Validate → Document → Close**

Investigations emphasize:

- Evidence collection
- Timeline development
- Analyst assessment
- Scope determination
- Escalation decisions
- Containment actions
- Remediation
- Post-response validation
- Final disposition

---

## Tier 1 SOC Capabilities

This lab demonstrates Tier 1 SOC analyst activities including:

- Alert monitoring
- Initial alert validation
- Security event triage
- Severity assessment
- False-positive identification
- Authentication investigation
- Endpoint telemetry review
- IOC identification and enrichment
- Incident documentation
- Escalation decisions
- Case closure

---

## Tier 2 SOC Capabilities

The lab also demonstrates Tier 2 investigation and response activities including:

- Multi-source investigation
- Linux log forensics
- Windows telemetry analysis
- Detection engineering
- Threat hunting
- MITRE ATT&CK analysis
- Detection tuning
- Scope determination
- Containment
- Remediation
- Defensive validation
- Automation and active response

---

## Technical Lab Coverage

The underlying technical environment includes:

- Wazuh
- Splunk Cloud
- Microsoft Sentinel
- Linux
- Windows
- Python
- KQL
- SPL
- REST APIs
- Network telemetry
- IOC enrichment
- fail2ban
- UFW
- SSH authentication monitoring
- MITRE ATT&CK

The technical components support the larger SOC workflow rather than existing as isolated infrastructure exercises.

---

## Evidence Philosophy

Investigations distinguish between:

- **Observed Evidence** — what the telemetry directly shows
- **Analyst Assessment** — the analyst's interpretation of the evidence
- **Inference** — conclusions supported by available evidence but not directly observed
- **Investigation Limitations** — what the available telemetry cannot establish

This approach is intended to demonstrate evidence-based SOC decision-making rather than simply documenting successful technical outcomes.

---

## Repository Structure

    SOC-Active-Response-Lab/
    ├── incidents/
    │   ├── README.md
    │   └── INC-001-SSH-Brute-Force/
    │       ├── case.md
    │       ├── timeline.md
    │       └── evidence.md
    │
    ├── triage/
    │   ├── severity-matrix.md
    │   ├── escalation-matrix.md
    │   └── evidence-standard.md
    │
    ├── week-1-wazuh-siem/
    ├── week-2-splunk-detection/
    ├── week-3-ssh-hardening/
    ├── week-4-windows-event-logs/
    ├── week-5-network-forensics/
    ├── week-6-ioc-enrichment/
    ├── week-7-soar-automation/
    ├── screenshots/
    └── README.md

---

## MITRE ATT&CK

Investigations and detection engineering activities are mapped to relevant MITRE ATT&CK techniques where appropriate.

Example techniques demonstrated within the lab include:

- T1110 — Brute Force
- T1110.001 — Password Guessing
- T1021.004 — SSH
- T1078 — Valid Accounts

MITRE mappings are used to provide investigative context and communicate attacker behavior rather than simply as a checklist.

---

## Current Focus

The current development focus is expanding the lab from a primarily technical security engineering environment into a complete SOC operations portfolio.

Planned investigation scenarios include:

- Windows suspicious execution
- Phishing investigation
- False-positive analysis
- Detection tuning
- Threat hunting
- Cross-source investigation
- Escalation and case management

---

## Security & Privacy

This repository contains controlled laboratory activity designed for defensive security research and SOC analyst training.

No production credentials, sensitive organizational information, or real-world confidential data should be included.

---

## Disclaimer

All attack simulations and defensive response activities are performed within controlled laboratory environments for cybersecurity education, detection engineering, and incident response training.
