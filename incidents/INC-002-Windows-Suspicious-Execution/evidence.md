# INC-002 — Windows Failed Logon Evidence Record

## Evidence Summary

This document records the evidence reviewed during the Windows failed-logon investigation.

Evidence must distinguish directly observed Windows authentication telemetry from analyst assessment, inference, and investigation limitations.

---

## 1. Detection Evidence

**Detection Source:** Splunk Cloud / Windows Security Event Logs

**Event ID:** 4625 — Failed Logon

**Detection Logic:**

The Splunk detection identifies repeated failed-logon activity:

```spl
index=main EventCode=4625
| stats count as failed_logons by src_ip, Account_Name
| where failed_logons > 5
| eval threat_level=if(failed_logons>15,"HIGH","MEDIUM")
| sort -failed_logons
```

**Observed Evidence:**

TBD — Record the actual alert, event count, source IP, account, host, and timestamps.

**Analyst Assessment:**

TBD — Determine whether the activity represents normal authentication failures or suspicious behavior.

---

## 2. Failed Authentication Evidence

**Event ID:** 4625

**Source IP:** TBD

**Target Account:** TBD

**Target Host:** TBD

**Logon Type:** TBD

**First Observed:** TBD

**Last Observed:** TBD

**Failed-Logon Count:** TBD

**Observed Evidence:**

TBD

**Analyst Assessment:**

TBD

---

## 3. Related Successful Authentication

**Event ID:** 4624 — Successful Logon

**Related Source IP:** TBD

**Target Account:** TBD

**Target Host:** TBD

**Logon Type:** TBD

**Timestamp:** TBD

**Observed Evidence:**

TBD — Document any successful authentication associated with the investigated activity.

**Analyst Assessment:**

TBD — Determine whether a successful logon is related to the failed-logon pattern. Do not assume compromise from an unrelated successful logon.

---

## 4. Authentication Context

**Observed Evidence:**

TBD

Investigated for:

- Repeated failed authentication
- Related successful authentication
- Privileged account targeting
- Account-specific activity
- Logon type and authentication pattern
- Unusual authentication timing

---

## 5. Scope Assessment

**Source IP:** TBD

**Affected Host:** TBD

**Target Account:** TBD

**Additional Hosts:** TBD

**Additional Accounts:** TBD

**Scope Determination:** TBD

---

## 6. Detection Assessment

**Configured Threshold:** More than 5 failed logons

**Threat-Level Logic:**

- MEDIUM: More than 5 failed logons
- HIGH: More than 15 failed logons

**Observed Detection Result:** TBD

**Analyst Assessment:** TBD

The configured detection threshold identifies activity requiring review. It does not independently confirm malicious activity.

---

## 7. Evidence Limitations


The investigation is limited to Windows Security Event Logs and supporting telemetry available within the lab environment.

Missing timestamps, source addresses, account details, or related authentication events must remain documented as unavailable until verified.

No successful authentication, credential compromise, or malicious activity will be claimed without supporting evidence.


---

## 8. Analyst Assessment

TBD

The final assessment will be based on observed Windows authentication events, Splunk detection results, related successful logons, and the confirmed investigation scope.

Observed evidence will be distinguished from analyst assessment and inference.

---

## 9. Evidence References

Related investigation documentation:

- [Case Record](case.md)
- [Investigation Timeline](timeline.md)

Supporting evidence should include:

- Windows Security Event ID 4625 records
- Related Event ID 4624 records
- Splunk detection results
- Relevant timestamps and screenshots
