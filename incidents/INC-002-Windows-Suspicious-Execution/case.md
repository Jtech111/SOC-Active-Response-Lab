# INC-002 — Windows Failed Logon Investigation

## Case Summary

| Field | Value |
|---|---|
| Case ID | INC-002 |
| Incident Type | Windows Failed Logon Investigation |
| Detection Source | Splunk Cloud / Windows Security Event Logs |
| Investigation Status | Open |
| Initial Severity | TBD |
| Final Severity | TBD |
| Disposition | TBD |
| Escalation | TBD |
| Affected Asset | TBD |
| Investigation Focus | Windows authentication activity and failed-logon patterns |

---

## 1. Alert

A Windows Security Event Log detection associated with repeated failed authentication attempts was identified for investigation.

The objective of this investigation is to determine whether the failed-logon activity represents normal user error, suspicious authentication behavior, or a potential brute-force pattern.

---

## 2. Initial Triage

### Detection Validation

The alert will be validated against Windows Security Event Logs and the associated Splunk detection logic.

The investigation will determine whether the observed failed-logon activity meets the detection threshold and whether the activity represents normal authentication behavior or suspicious activity.

### Initial Assessment

The activity requires investigation to determine:

- Failed-logon count
- Source IP address
- Target account
- Target host
- Time range of activity
- Logon type
- Related successful logons
- Related authentication events
- Whether the pattern is consistent with brute-force activity

### Initial Severity

**TBD**

Severity will be determined after reviewing the available evidence.

---

## 3. Investigation

The investigation will review Windows Security Event Logs and Splunk telemetry associated with the failed-logon activity.

The investigation will examine:

- Event ID 4625 failed-logon events
- Failed-logon volume and frequency
- Source IP address
- Target account
- Target host
- Logon type
- Time range and activity pattern
- Related Event ID 4624 successful logons
- Related authentication events
- Whether the activity exceeds the configured detection threshold
- Whether the pattern is consistent with brute-force or password-guessing activity

The investigation will correlate available authentication events to determine whether the activity represents isolated authentication failures or a broader security event.

---

## 4. Scope Assessment

### Source

**TBD**

The source IP associated with the failed-logon activity will be identified from the available Windows Security Event telemetry.

### Target

**TBD**

The affected Windows host and targeted account will be identified from the authentication events.

### Authentication Activity

**TBD**

The investigation will determine the number, frequency, and timing of failed authentication attempts and identify any related successful logons.

### Logon Type

**TBD**

The applicable Windows logon type will be identified and assessed in the context of the observed activity.

### Additional Compromise Indicators

**TBD**

The investigation will assess available telemetry for evidence of successful authentication, privileged account activity, additional affected systems, or other indicators of compromise.

---

## 5. Analyst Assessment

**TBD**

The analyst assessment will determine whether the observed authentication activity is consistent with:

- Normal user authentication behavior
- Suspicious authentication activity
- Password guessing
- Brute-force activity
- Confirmed compromise

The assessment will be based on observed Windows Security Event telemetry, Splunk detection results, authentication patterns, and available supporting evidence.

Observed evidence will be distinguished from analyst assessment and inference.

---

## 6. MITRE ATT&CK Mapping

| Technique | Description | Evidence |
|---|---|---|
| T1110.001 | Password Guessing | TBD — requires investigation evidence showing a repeated failed-logon pattern |
| T1078 | Valid Accounts | TBD — only applicable if successful authentication is identified in related telemetry |

MITRE ATT&CK techniques will only be assigned as confirmed findings when supported by investigation evidence.

---

## 7. Response

**TBD**

Response actions will be determined based on the confirmed scope and severity of the authentication activity.

Potential response considerations include:

- Confirming whether the source is authorized
- Reviewing the targeted account
- Validating whether successful authentication occurred
- Applying appropriate account or network controls when malicious activity is confirmed
- Escalating when evidence indicates credential compromise or broader attack activity

No response action will be documented as completed unless supported by observed evidence.

---

## 8. Validation

**TBD**

Post-response validation will determine whether the failed-logon activity has stopped or whether additional suspicious authentication activity remains.

Validation may include:

- Reviewing subsequent Event ID 4625 activity
- Checking for related Event ID 4624 successful logons
- Confirming whether the source continues generating authentication failures
- Reviewing the affected account for additional suspicious activity
- Confirming that any defensive action produced the expected result

---

## 9. Escalation Decision

**TBD**

Escalation will be considered if investigation evidence identifies:

- High-volume or sustained failed-logon activity
- Successful authentication associated with the failed-logon pattern
- Evidence of password guessing or brute-force activity
- Privileged account targeting
- Credential compromise
- Multiple affected hosts or accounts
- Suspicious activity from an unauthorized source
- Evidence of lateral movement
- Additional indicators of compromise

The escalation decision will be based on the documented severity and available evidence.

---

## 10. Final Disposition

**TBD**

The final disposition will be based on the completed investigation and supporting evidence.

Possible dispositions include:

- Benign Authentication Activity
- Suspicious Activity — No Confirmed Compromise
- Confirmed Brute-Force Activity
- Confirmed Credential Compromise
- False Positive
- Escalated for Additional Investigation

---

## 11. Evidence References

Supporting evidence should include:

- Windows Security Event ID 4625 records
- Related Event ID 4624 records
- Source IP information
- Target account information
- Target host information
- Logon type
- Authentication timestamps
- Splunk detection results
- Relevant screenshots
- Related authentication or network telemetry

Detailed evidence and timestamps are documented in:

- [Investigation Timeline](timeline.md)
- [Evidence Record](evidence.md)

Evidence should distinguish directly observed telemetry from analyst assessment, inference, and investigation limitations.
