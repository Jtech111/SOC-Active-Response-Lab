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
| Investigation Focus | Process execution and supporting Windows telemetry |

---

## 1. Alert

A Windows security event or detection associated with suspicious process execution was identified for investigation.

The objective of this investigation is to determine whether the execution represents benign administrative activity, suspicious behavior, or confirmed malicious activity.

---

## 2. Initial Triage

### Detection Validation

The alert will be validated against the available Windows telemetry and associated security events.

### Initial Assessment

The activity requires investigation to determine:

- Executed process
- Parent process
- User context
- Command-line activity
- Execution time
- Affected host
- Related events

### Initial Severity

**TBD**

Severity will be determined after reviewing the available evidence.

---

## 3. Investigation

The investigation will review:

- Windows event telemetry
- Process execution data
- Parent/child process relationships
- Command-line information
- User context
- Host information
- Related authentication activity
- Related network activity
- Available security alerts

---

## 4. Scope Assessment

### Source

**TBD**

### Target

**TBD**

### User Context

**TBD**

### Process Execution

**TBD**

### Additional Compromise Indicators

**TBD**

---

## 5. Analyst Assessment

**TBD**

The analyst assessment will be based on observed telemetry and documented evidence.

---

## 6. MITRE ATT&CK Mapping

| Technique | Description | Evidence |
|---|---|---|
| TBD | TBD | TBD |

MITRE ATT&CK techniques will only be assigned when supported by the investigation evidence.

---

## 7. Response

**TBD**

Response actions will be determined based on the confirmed scope and severity of the activity.

---

## 8. Validation

**TBD**

Post-response validation will determine whether the activity was successfully contained or whether additional investigation is required.

---

## 9. Escalation Decision

**TBD**

Escalation will be considered if investigation evidence identifies:

- Confirmed malicious execution
- Credential compromise
- Persistence
- Lateral movement
- Privileged account involvement
- Additional affected systems
- Confirmed malware
- Evidence of broader compromise

---

## 10. Final Disposition

**TBD**

The final disposition will be based on the completed investigation.

---

## 11. Evidence References

Supporting evidence should include:

- Windows event logs
- Process execution telemetry
- Command-line evidence
- Sentinel alerts or incidents
- Relevant screenshots
- Related network or authentication telemetry

Detailed evidence and timestamps will be documented in:

- [Timeline](timeline.md)
- [Evidence](evidence.md)
