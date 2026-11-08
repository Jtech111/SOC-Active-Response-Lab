# SOC Severity Matrix

## Purpose

This framework defines how alerts are assessed and assigned an operational severity during Tier 1/2 SOC triage.

SIEM-generated alert severity is treated as an input to analyst triage, not automatically as the final incident severity.

---

## Severity Levels

| Severity | General Meaning | Typical Analyst Action |
|---|---|---|
| LOW | Suspicious or low-impact activity with limited evidence of compromise | Review, validate, document |
| MEDIUM | Credible malicious or suspicious activity requiring investigation | Investigate, scope, document |
| HIGH | Strong evidence of compromise, successful attack activity, or significant risk | Immediate investigation and Tier 2 escalation |
| CRITICAL | Confirmed compromise involving critical systems, privileged access, widespread impact, or active threat | Immediate escalation and containment |

---

## Severity Assessment Factors

The analyst should consider:

1. Detection confidence
2. Asset criticality
3. Account sensitivity
4. Number of affected hosts
5. Number of affected accounts
6. Successful versus failed activity
7. Evidence of persistence
8. Evidence of lateral movement
9. Evidence of credential compromise
10. Business or operational impact

---

## Analyst Decision Rule

Severity should be based on the totality of available evidence.

A high-volume alert does not automatically mean a high-severity incident.

The analyst should determine:

- What happened?
- Did the activity succeed?
- What system or account was targeted?
- How many assets are affected?
- Is there evidence of compromise?
- Is the activity ongoing?
- Does the event require escalation?

---

## Required Documentation

Every triaged alert should document:

- Alert source
- Detection
- Timestamp
- Source IP or entity
- Target host or account
- Initial severity
- Analyst-assigned severity
- Evidence supporting the decision
- Scope
- Escalation decision
- Containment or response action
- Final disposition

---

## Example: SSH Brute Force

The lab demonstrates repeated failed SSH authentication attempts against a Linux endpoint.

The documented attack produced Wazuh correlation alerts indicating brute-force behavior. The investigation also confirmed:

- The attacker IP generated repeated failed authentication attempts.
- The targeted username was identified.
- No successful attacker login was observed.
- Legitimate administrator activity was distinguishable from attacker activity.
- The attack was subsequently mitigated through defensive controls.

### Initial Assessment

**Category:** Brute Force / Credential Access

**Initial Severity:** MEDIUM

**Escalation:** Based on evidence of successful authentication, privileged account targeting, persistence, lateral movement, or additional affected systems.

### Analyst Principle

Failed authentication alone does not prove account compromise.

The analyst must validate whether authentication succeeded before determining whether the incident represents an attempted attack or confirmed compromise.
