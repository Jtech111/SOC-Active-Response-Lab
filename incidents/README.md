# SOC Incident Cases

This directory contains documented security investigations conducted within the SOC lab.

Each case follows a structured investigation process:

**Detect → Triage → Investigate → Scope → Classify → Respond → Validate → Document → Close**

---

## Incident Register

| Case ID | Investigation | Severity | Disposition | Status |
|---|---|---|---|---|
| INC-001 | SSH Brute-Force | Medium | Confirmed Malicious Activity | Closed |
| INC-002 | Windows Failed Logon Investigation | TBD | TBD | Open |
| INC-003 | Phishing Investigation | TBD | TBD | Open |

---

## Case Documentation

### INC-001 — SSH Brute-Force

A controlled investigation of repeated SSH authentication failures against a monitored Linux host.

- [Case Record](INC-001-SSH-Brute-Force/case.md)
- [Investigation Timeline](INC-001-SSH-Brute-Force/timeline.md)
- [Evidence Record](INC-001-SSH-Brute-Force/evidence.md)

### INC-002 — Windows Failed Logon Investigation

A structured Windows authentication investigation focused on failed logon activity, Event ID 4625, successful-logon correlation, scope assessment, and escalation criteria.

- [Case Record](INC-002-Windows-Suspicious-Execution/case.md)
- [Investigation Timeline](INC-002-Windows-Suspicious-Execution/timeline.md)
- [Evidence Record](INC-002-Windows-Suspicious-Execution/evidence.md)

### INC-003 — Phishing Investigation

A structured email security investigation focused on phishing indicators, authentication results, user interaction, enrichment, scope, response, and validation.

- [Case Record](INC-003-Phishing-Investigation/case.md)
- [Investigation Timeline](INC-003-Phishing-Investigation/timeline.md)
- [Evidence Record](INC-003-Phishing-Investigation/evidence.md)

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

---

## Case Management Principles

Cases should be treated as operational records rather than technical write-ups.

Analysts should document:

1. What was detected
2. Why it was suspicious
3. What evidence was reviewed
4. What systems or users were affected
5. How severity was determined
6. Whether escalation was required
7. What response actions were taken
8. How response effectiveness was validated
9. Why the case was closed or escalated

Where evidence is unavailable, the case should explicitly document the limitation rather than inventing investigative results.
