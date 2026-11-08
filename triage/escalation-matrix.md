# SOC Escalation Matrix

## Purpose

This framework defines when a Tier 1 analyst should continue investigation and when an alert or incident should be escalated to Tier 2 or higher.

---

## Tier 1 Responsibilities

Tier 1 should:

1. Acknowledge the alert
2. Validate the detection
3. Identify the affected asset or account
4. Review relevant telemetry
5. Determine whether the activity is suspicious, benign, or malicious
6. Check for successful versus failed activity
7. Determine initial scope
8. Enrich available indicators
9. Document findings
10. Escalate when defined criteria are met

---

## Tier 2 Responsibilities

Tier 2 should become involved when deeper investigation or response is required, including:

- Confirmed compromise
- Successful authentication following suspicious activity
- Suspicious process execution
- Persistence
- Lateral movement
- Privileged account compromise
- Credential theft
- Multiple affected systems
- Malware execution
- Significant endpoint or network impact
- Complex investigation requiring additional telemetry
- Detection logic requiring engineering changes

---

## Escalation Criteria

| Condition | Tier 1 Action |
|---|---|
| Repeated failed authentication only | Investigate and document |
| Brute-force pattern with no successful login | Investigate, scope, document |
| Successful login from suspicious source | Escalate to Tier 2 |
| Suspicious PowerShell execution | Escalate if malicious indicators or unusual context are present |
| Confirmed malware execution | Escalate immediately |
| Persistence identified | Escalate immediately |
| Lateral movement suspected | Escalate immediately |
| Privileged account compromise | Escalate immediately |
| Multiple affected endpoints | Escalate |
| Phishing with confirmed credential compromise | Escalate |
| Detection produces excessive false positives | Document and submit for detection tuning |

---

## Minimum Escalation Package

Before escalating, the analyst should provide:

### Alert Information

- Alert name
- Detection source
- Detection timestamp
- Severity
- Source entity
- Destination/target entity

### Investigation Summary

- What happened?
- What evidence was observed?
- What was confirmed?
- What remains unknown?
- What systems/accounts are affected?

### Timeline

Document significant events in chronological order.

### Evidence

Include relevant:

- SIEM events
- Endpoint logs
- Network telemetry
- Authentication records
- Process information
- Screenshots
- Command output

### Analyst Assessment

State clearly:

- Confirmed
- Suspected
- Benign
- False positive
- Unable to determine

### Recommended Next Action

Explain what Tier 2 should investigate or perform next.

---

## Escalation Principle

Do not escalate simply because an alert looks severe.

Escalate when the available evidence indicates that additional investigation, response authority, or technical expertise is required.
