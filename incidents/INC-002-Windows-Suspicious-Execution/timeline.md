# INC-002 — Windows Failed Logon Investigation Timeline

## Timeline

| Time | Event | Source | Analyst Action |
|---|---|---|---|
| TBD | Repeated Windows failed-logon activity detected | Windows Security Event ID 4625 / Splunk | Alert received and queued for triage |
| TBD | Detection validated against available telemetry | Splunk / Windows Security logs | Confirmed supporting authentication events |
| TBD | Failed-logon pattern reviewed | Windows Security Event ID 4625 | Reviewed source IP, account, host, timing, and volume |
| TBD | Related authentication activity investigated | Windows Security Event IDs 4624 / 4625 | Reviewed for successful authentication and related activity |
| TBD | Scope assessed | Windows / Splunk telemetry | Determined affected host, account, source, and activity range |
| TBD | Analyst assessment completed | Case evidence | Classified activity based on observed evidence |
| TBD | Response decision documented | Case documentation | Determined whether response or escalation was required |
| TBD | Post-response validation performed | Windows / Splunk telemetry | Reviewed subsequent authentication activity |
| TBD | Case disposition recorded | Case documentation | Investigation closed or escalated |

---

## Investigation Phases

### Detection

**TBD**

Document the initial Event ID 4625 detection and the Splunk detection that identified the failed-logon pattern.

### Triage

**TBD**

Document the initial validation, failed-logon volume, source, target account, host, logon type, and initial severity.

### Investigation

**TBD**

Document authentication-event analysis, related Event ID 4624 activity, timing, frequency, and evidence supporting or refuting brute-force behavior.

### Scope

**TBD**

Document affected hosts, accounts, source IPs, authentication activity, and any additional indicators identified.

### Response

**TBD**

Document any defensive action taken or explain why no response action was required.

### Validation

**TBD**

Document post-response telemetry review and whether suspicious authentication activity continued.

### Closure

**TBD**

Document final classification, disposition, escalation decision, and investigation limitations.
