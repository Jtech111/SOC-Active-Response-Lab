# SOC Evidence Standard

## Purpose

This document defines how evidence is collected, classified, documented, and referenced during SOC investigations.

The objective is to maintain an evidence-first investigation process and prevent unsupported conclusions.

---

## Evidence Classification

### Observed

Directly supported by available telemetry, logs, screenshots, command output, or other evidence.

Example:

> `auth.log` shows repeated failed SSH authentication attempts from the identified source IP.

---

### Analyst Assessment

A conclusion reached by analyzing available evidence.

Example:

> The authentication pattern is consistent with an SSH brute-force attempt.

---

### Inferred

A reasonable conclusion that is not directly proven by available evidence.

Inferences must be clearly identified as such.

---

### Not Observed

The investigation specifically checked for an event but did not find evidence of it.

Example:

> No successful authentication from the attacker IP was observed in the reviewed authentication logs.

---

### Unable to Determine

Available telemetry was insufficient to confirm or deny the condition.

Example:

> Unable to determine whether the same credential was attempted against other hosts because telemetry was not available.

---

## Required Investigation Evidence

Whenever applicable, document:

- Detection source
- Alert timestamp
- Source IP or entity
- Destination host
- Target account
- Relevant log entries
- Detection rule
- Authentication outcome
- Process activity
- Network activity
- IOC information
- Scope
- Containment action
- Validation results
- Final disposition

---

## Evidence Hierarchy

When available, prioritize:

1. Raw endpoint logs
2. SIEM events
3. Endpoint telemetry
4. Network telemetry
5. Command output
6. Screenshots
7. Analyst notes
8. Derived conclusions

---

## Screenshot Standard

Screenshots should demonstrate an actual investigation result.

Useful screenshots include:

- SIEM alert
- Relevant event details
- Authentication logs
- Process information
- Network evidence
- Detection query
- Containment action
- Validation after remediation

Screenshots should be accompanied by text explaining what the evidence demonstrates.

---

## Claim Standard

Avoid unsupported statements such as:

> "The system was compromised."

unless evidence confirms compromise.

Prefer:

> "Repeated failed authentication attempts were observed, but no successful attacker authentication was identified in the reviewed logs."

---

## Missing Telemetry

If required evidence is unavailable, document the limitation.

Example:

> Endpoint process telemetry was not available for this investigation, so process execution could not be confirmed.

Missing evidence should not be replaced with assumptions.

---

## Evidence-First Principle

The investigation should distinguish clearly between:

**What was observed**

**What was determined**

**What was inferred**

**What was not observed**

**What could not be determined**

This distinction is required for defensible SOC reporting.
