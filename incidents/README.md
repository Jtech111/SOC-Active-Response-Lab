# SOC Incident Cases

This directory contains documented security investigations conducted within the SOC lab.

Each case follows a structured investigation process:

**Detect → Triage → Investigate → Scope → Classify → Respond → Validate → Document → Close**

---

## Incident Register

| Case ID | Investigation | Severity | Disposition | Status |
|---|---|---|---|---|
| INC-001 | SSH Brute-Force | Medium | Confirmed Malicious Activity | Closed |

---

## Case Documentation

### INC-001 — SSH Brute-Force

A controlled investigation of repeated SSH authentication failures against a monitored Linux host.

- [Case Record](INC-001-SSH-Brute-Force/case.md)
- [Investigation Timeline](INC-001-SSH-Brute-Force/timeline.md)
- [Evidence Record](INC-001-SSH-Brute-Force/evidence.md)

---

## Investigation Standard

Each case should document:

- Detection
- Initial triage
- Severity assessment
- Investigation scope
- Evidence
- Analyst assessment
- Escalation decision
- Response
- Validation
- Final disposition

Cases should distinguish observed evidence from analyst assessment, inference, and investigation limitations.
