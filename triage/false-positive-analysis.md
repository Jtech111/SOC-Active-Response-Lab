# SOC False Positive Analysis & Alert Tuning

## Purpose

This document defines the analyst process for evaluating false-positive security alerts and improving detection quality without reducing meaningful coverage.

False-positive analysis is treated as an operational SOC activity involving:

**Detect → Triage → Validate → Investigate → Classify → Tune → Validate → Document**

---

## 1. Alert Under Review

| Field | Value |
|---|---|
| Detection | Windows Failed Logon Detection |
| Detection Source | Splunk Cloud |
| Primary Event | Windows Event ID 4625 |
| Detection Logic | More than 5 failed logons by source IP and account |
| Current Severity | MEDIUM / HIGH based on failure volume |
| Review Status | Planned |

---

## 2. Why the Alert May Generate False Positives

Failed authentication events can occur for legitimate reasons, including:

- User password mistakes
- Expired credentials
- Service account authentication failures
- Scheduled tasks using outdated credentials
- Mapped drives using stale credentials
- Administrative activity
- Misconfigured applications
- Automated systems repeatedly attempting authentication

A failed logon alert should therefore be evaluated in context rather than treated as confirmed malicious activity.

---

## 3. Tier 1 Triage

The analyst should review:

- Source IP
- Destination host
- Account name
- Failure count
- Time range
- Logon type
- Authentication pattern
- Related successful logons
- User or service-account context
- Additional alerts from the same source

### Initial Questions

1. Is the source expected?
2. Is the account expected on the target system?
3. Is the activity consistent with normal user behavior?
4. Is the failure pattern automated?
5. Did successful authentication follow the failures?
6. Are multiple accounts being targeted?
7. Is the source associated with other suspicious activity?

---

## 4. False-Positive Determination

An alert may be classified as a false positive when available evidence demonstrates that the activity is legitimate and no indicators of compromise are identified.

Examples include:

- Known administrative workstation
- Approved service account
- Documented scheduled task
- Known application authentication issue
- User-confirmed password error
- Expected maintenance activity

**Disposition:** TBD

**Evidence Supporting Disposition:** TBD

---

## 5. True Positive Indicators

The alert should remain suspicious when evidence includes:

- Multiple accounts targeted
- High-volume authentication failures
- Unknown source system
- Unusual source location
- Password guessing pattern
- Failed logons followed by successful authentication
- Privileged account targeting
- Authentication activity outside expected behavior
- Related endpoint or network alerts

---

## 6. Detection Tuning

Potential tuning improvements include:

- Establishing approved administrative source allowlists
- Separating service-account behavior from interactive user behavior
- Adding logon-type analysis
- Correlating Event ID 4625 with Event ID 4624
- Increasing severity when multiple accounts are targeted
- Increasing severity when successful authentication follows repeated failures
- Reducing severity for documented benign sources
- Adding time-window and frequency thresholds
- Correlating with endpoint or network telemetry

Tuning should reduce unnecessary analyst workload while preserving detection coverage.

---

## 7. Before / After Evaluation

### Before Tuning

**Alert Volume:** TBD

**False-Positive Rate:** TBD

**Primary Noise Source:** TBD

**Analyst Impact:** TBD

### After Tuning

**Alert Volume:** TBD

**False-Positive Rate:** TBD

**Detection Coverage:** TBD

**Analyst Impact:** TBD

---

## 8. Validation

After a detection change, validate that:

- Known benign activity no longer creates unnecessary alerts
- Expected malicious patterns still generate alerts
- Thresholds behave as intended
- Severity assignment remains appropriate
- Important Event IDs remain visible
- Related authentication activity is still correlated

**Validation Result:** TBD

---

## 9. Analyst Decision

### Classification

**True Positive / False Positive / Benign / Inconclusive:** TBD

### Analyst Assessment

TBD

### Confidence

**Low / Medium / High:** TBD

### Escalation Required

**Yes / No:** TBD

### Reason

TBD

---

## 10. Evidence Discipline

Analysts should distinguish:

### Observed Evidence

Facts directly supported by telemetry.

### Analyst Assessment

Professional interpretation of observed evidence.

### Inference

A conclusion requiring additional validation.

### Investigation Limitation

Missing or incomplete telemetry that prevents a definitive conclusion.

No tuning decision should be based solely on assumptions.

---

## 11. MITRE ATT&CK Context

Potentially relevant techniques include:

- **T1110 — Brute Force**
- **T1110.001 — Password Guessing**
- **T1078 — Valid Accounts**

Final ATT&CK mapping should be based on observed activity.

---

## 12. Operational Outcome

The goal of alert tuning is not simply to reduce alert volume.

A successful tuning change should:

- Reduce unnecessary analyst workload
- Improve signal-to-noise ratio
- Preserve meaningful detection coverage
- Improve severity accuracy
- Improve investigation efficiency
- Produce documented and repeatable analyst decisions

**Final Outcome:** TBD
