# INC-003 — Phishing Investigation

## Case Summary

| Field | Value |
|---|---|
| Case ID | INC-003 |
| Incident Type | Phishing / Suspicious Email |
| Detection Source | Email Security / User Report / SIEM |
| Investigation Status | Open |
| Initial Severity | TBD |
| Final Severity | TBD |
| Disposition | TBD |
| Escalation Tier | Tier 1 Investigation / Tier 2 Escalation if required |
| Affected User | TBD |
| Investigation Focus | Email characteristics, sender, URLs, attachments, user interaction, and potential account compromise |

---

## 1. Detection

A suspicious email was identified through available email security telemetry and/or user reporting.

Initial triage should determine whether the message exhibits characteristics consistent with phishing, credential theft, malicious attachment delivery, business email compromise, or other social-engineering activity.

---

## 2. Initial Triage

The analyst should review:

- Sender address and sender domain
- Recipient
- Subject
- Timestamp
- Email authentication results
- URLs and domains
- Attachments
- Display-name spoofing
- Reply-to address
- Message headers
- User interaction indicators
- Related security alerts

### Initial Assessment

**Status:** TBD

**Analyst Assessment:** TBD

**Reason for Severity:** TBD

---

## 3. Investigation

The investigation should determine whether the email is malicious and whether the recipient interacted with the content.

### Email Analysis

Review:

- Sender identity
- Sending infrastructure
- SPF result
- DKIM result
- DMARC result
- URL destinations
- Attachment characteristics
- Domain reputation
- Message content
- Social-engineering indicators

### User Activity

Determine whether the recipient:

- Opened the message
- Clicked a URL
- Opened an attachment
- Submitted credentials
- Replied to the sender
- Reported the message
- Performed any other potentially risky action

---

## 4. Scope

Determine whether the activity affected:

- Additional recipients
- Additional mailboxes
- Additional users
- Endpoints
- User credentials
- Cloud identities
- Other internal systems

### Scope Assessment

**Known Affected Users:** TBD

**Known Affected Systems:** TBD

**Additional Recipients Identified:** TBD

**Evidence of Account Compromise:** TBD

---

## 5. Enrichment

Available indicators should be evaluated using approved threat-intelligence sources.

Potential indicators include:

- Sender IP
- Sender domain
- Reply-to address
- URL
- Domain
- File hash
- Attachment name
- Attachment hash

### Enrichment Results

**Reputation:** TBD

**Threat Intelligence:** TBD

**Related Activity:** TBD

---

## 6. MITRE ATT&CK Mapping

Potential techniques may include:

- **T1566 — Phishing**
- **T1566.001 — Spearphishing Attachment**
- **T1566.002 — Spearphishing Link**
- **T1566.003 — Spearphishing via Service**
- **T1078 — Valid Accounts** if credential compromise is identified

Final technique mapping should be based on observed evidence rather than assumptions.

---

## 7. Escalation Criteria

Escalate to Tier 2 or incident response when evidence indicates:

- User credentials were submitted
- Malicious attachment was executed
- Malicious URL was accessed
- Account compromise is suspected
- Additional users received the message
- Endpoint compromise is suspected
- Persistence is identified
- Suspicious authentication follows the phishing event
- Business email compromise is suspected
- Privileged or sensitive accounts are involved

---

## 8. Response

Potential response actions include:

- Quarantine or remove malicious email
- Block malicious sender/domain
- Block malicious URLs
- Remove malicious attachments
- Reset compromised credentials
- Revoke active sessions
- Investigate affected endpoint
- Review authentication activity
- Notify affected users
- Search for additional recipients

**Response Status:** TBD

---

## 9. Validation

After response actions, validate that:

- The message is no longer accessible to affected users
- Malicious indicators are blocked
- No additional recipients remain exposed
- No suspicious authentication activity continues
- No endpoint compromise is identified
- Any compromised credentials have been remediated
- Detection coverage is functioning as expected

**Validation Result:** TBD

---

## 10. Evidence and Limitations

All conclusions should distinguish between:

- **Observed Evidence** — directly supported by available telemetry
- **Analyst Assessment** — professional interpretation of observed evidence
- **Inference** — conclusions that require additional validation
- **Investigation Limitations** — unavailable or incomplete telemetry

Evidence should be documented in:

- [Investigation Timeline](timeline.md)
- [Evidence Record](evidence.md)

---

## 11. Final Disposition

**Final Severity:** TBD

**Disposition:** TBD

**Escalation Decision:** TBD

**Closure Status:** TBD

### Analyst Conclusion

TBD

The case should remain open until sufficient evidence supports classification, response, validation, and closure.
