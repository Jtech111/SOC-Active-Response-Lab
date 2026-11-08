# INC-001 — SSH Brute-Force Investigation

## Case Summary

| Field | Value |
|---|---|
| Case ID | INC-001 |
| Incident Type | SSH Brute-Force |
| Detection Source | Wazuh |
| Investigation Status | Closed |
| Initial Severity | Medium |
| Final Severity | Medium |
| Disposition | Confirmed Malicious Activity |
| Escalation | Tier 1 Investigation / Tier 2 Review if required |
| Affected Service | SSH |
| Investigation Focus | Authentication activity and defensive response |

---

## 1. Alert

A Wazuh detection identified repeated failed SSH authentication attempts against a monitored Linux host.

The alert was investigated to determine whether the activity represented automated credential guessing, whether authentication succeeded, and whether additional compromise indicators were present.

---

## 2. Initial Triage

### Detection Validation

The alert was validated against Linux authentication telemetry.

Observed activity included repeated failed SSH authentication attempts originating from the identified attack source.

### Initial Assessment

The activity was assessed as suspicious and consistent with an automated SSH brute-force attempt.

### Initial Severity

**Medium**

The activity represented credible malicious behavior requiring investigation and scoping, but no successful attacker authentication was identified in the reviewed evidence.

---

## 3. Investigation

The investigation reviewed:

- SSH authentication logs
- Wazuh alert telemetry
- Source IP information
- Authentication outcomes
- Attack timing
- Repeated authentication attempts
- Defensive control behavior

The attack pattern was consistent with automated SSH credential guessing.

---

## 4. Scope Assessment

### Source

The identified source generated repeated SSH authentication attempts against the monitored host.

### Target

The activity targeted the monitored Linux SSH service.

### Authentication Result

The reviewed authentication evidence showed repeated failed authentication attempts.

No successful attacker authentication was identified in the reviewed evidence.

### Additional Compromise Indicators

No additional compromise indicators were identified within the available investigation evidence.

---

## 5. Analyst Assessment

**Confirmed Malicious Activity**

The observed authentication pattern was consistent with an automated SSH brute-force attack.

The investigation did not identify evidence of successful attacker authentication.

---

## 6. MITRE ATT&CK Mapping

| Technique | Description | Evidence |
|---|---|---|
| T1110 | Brute Force | Repeated authentication attempts |
| T1110.001 | Password Guessing | Automated SSH credential attempts |
| T1021.004 | SSH | SSH service targeted |
| T1078 | Valid Accounts | Reviewed as a potential authentication outcome |

---

## 7. Response

Defensive controls were applied to reduce the effectiveness of the attack.

Response actions included:

- fail2ban configuration
- SSH configuration hardening
- UFW firewall controls

The response was followed by additional attack testing to validate defensive effectiveness.

---

## 8. Validation

Post-response testing demonstrated that the defensive controls interrupted the repeated attack activity earlier than the original test.

The documented testing showed the attack being stopped at approximately attempt 14 after hardening, compared with approximately 24 attempts during the original test.

This provided validation that the implemented controls reduced the attack's effectiveness.

---

## 9. Escalation Decision

The investigation did not identify successful authentication, persistence, lateral movement, or confirmed host compromise within the available evidence.

Based on the observed scope and available evidence, the incident did not require immediate emergency escalation.

The case should be escalated if subsequent telemetry identifies:

- Successful authentication
- Credential compromise
- Persistence
- Lateral movement
- Additional affected systems
- Privileged account involvement
- Evidence of host compromise

---

## 10. Final Disposition

**Confirmed Malicious Activity — Contained**

The investigation confirmed malicious SSH brute-force activity.

No successful attacker authentication was identified in the reviewed evidence.

Defensive controls were implemented and validated through repeat testing.

---

## 11. Evidence References

Supporting evidence should include:

- Wazuh alert screenshots
- Linux authentication log evidence
- Attack testing output
- Defensive configuration changes
- Post-hardening validation results

Detailed evidence and timestamps are documented in:

- [Timeline](timeline.md)
- [Evidence](evidence.md)
