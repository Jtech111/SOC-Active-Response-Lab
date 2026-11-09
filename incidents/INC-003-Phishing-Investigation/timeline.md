# INC-003 — Phishing Investigation Timeline

## Timeline

| Time | Event | Source | Analyst Action |
|---|---|---|---|
| TBD | Suspicious email detected or reported | Email Security / User Report | Alert received and queued for triage |
| TBD | Sender and message characteristics reviewed | Email telemetry | Reviewed sender, recipient, subject, domain, and message content |
| TBD | Email authentication evaluated | Email headers | Reviewed SPF, DKIM, and DMARC results |
| TBD | URLs and attachments reviewed | Email telemetry | Identified and assessed potentially malicious indicators |
| TBD | Threat intelligence enrichment performed | Threat Intelligence | Evaluated domains, URLs, IPs, and hashes where available |
| TBD | User interaction assessed | Endpoint / Identity / Email telemetry | Determined whether links, attachments, or credentials were accessed |
| TBD | Scope assessed | Email / SIEM / Identity telemetry | Checked for additional recipients and related activity |
| TBD | Containment actions performed | Email Security / Identity / Endpoint controls | Quarantined, blocked, or remediated confirmed malicious activity |
| TBD | Post-response validation performed | Email / Identity / Endpoint telemetry | Confirmed response effectiveness and checked for continued activity |
| TBD | Investigation disposition determined | Case record | Classified, escalated, or closed based on available evidence |

---

## Detection

A suspicious email was identified through available email security telemetry and/or user reporting.

**Detection Status:** TBD

---

## Triage

The analyst reviewed:

- Sender address
- Sender domain
- Recipient
- Subject
- Timestamp
- Email authentication
- URLs
- Attachments
- Reply-to address
- Initial user interaction indicators

**Initial Severity:** TBD

**Initial Assessment:** TBD

---

## Investigation

The investigation focused on determining whether the email was malicious and whether the recipient interacted with potentially harmful content.

### Email Analysis

- Sender identity: TBD
- Sender infrastructure: TBD
- SPF: TBD
- DKIM: TBD
- DMARC: TBD
- URLs: TBD
- Attachments: TBD
- Domain reputation: TBD
- Message characteristics: TBD

### User Activity

- Email opened: TBD
- URL clicked: TBD
- Attachment opened: TBD
- Credentials submitted: TBD
- Reply sent: TBD

---

## Scope

The analyst assessed whether the phishing activity affected:

- Additional recipients
- Additional mailboxes
- User credentials
- Cloud identities
- Endpoints
- Other internal systems

**Scope Result:** TBD

---

## Enrichment

Available indicators were evaluated using approved threat-intelligence sources.

**Enrichment Result:** TBD

---

## Response

Potential response actions included:

- Email quarantine or removal
- Sender/domain blocking
- URL blocking
- Attachment removal
- Credential reset
- Session revocation
- Endpoint investigation
- Authentication review
- User notification

**Response Result:** TBD

---

## Validation

Following response actions, the analyst validated:

- Malicious email removal
- Indicator blocking
- Additional recipient exposure
- Authentication activity
- Endpoint activity
- Credential remediation
- Detection coverage

**Validation Result:** TBD

---

## Escalation

Escalation to Tier 2 or incident response is required if evidence indicates:

- Credential compromise
- Malicious attachment execution
- Malicious URL access
- Account compromise
- Endpoint compromise
- Persistence
- Suspicious authentication
- Business email compromise
- Privileged account involvement

**Escalation Decision:** TBD

---

## Closure

**Final Severity:** TBD

**Final Disposition:** TBD

**Closure Status:** TBD

**Analyst Conclusion:** TBD

The case should remain open until sufficient evidence supports classification, response, validation, and closure.

---

## Evidence References

- [Case Record](case.md)
- [Evidence Record](evidence.md)
