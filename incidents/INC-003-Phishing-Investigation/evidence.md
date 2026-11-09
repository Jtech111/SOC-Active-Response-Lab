# INC-003 — Phishing Investigation Evidence Record

## 1. Detection Evidence

**Evidence Type:** Suspicious email detection/report

**Source:** Email Security / User Report / SIEM

**Observed Evidence:** TBD

**Analyst Assessment:** The initial email characteristics should be reviewed to determine whether the message is consistent with phishing activity.

---

## 2. Email Metadata

| Evidence | Value |
|---|---|
| Sender | TBD |
| Sender Domain | TBD |
| Recipient | TBD |
| Subject | TBD |
| Timestamp | TBD |
| Reply-To | TBD |
| Message ID | TBD |

---

## 3. Authentication Evidence

| Control | Result |
|---|---|
| SPF | TBD |
| DKIM | TBD |
| DMARC | TBD |

Authentication results should be interpreted together with sender identity, infrastructure, message content, and other available telemetry.

---

## 4. Indicator Evidence

Potential indicators identified during investigation:

- Sender IP: TBD
- Sender domain: TBD
- URL: TBD
- Attachment name: TBD
- File hash: TBD
- Domain reputation: TBD

**Threat Intelligence Result:** TBD

---

## 5. User Interaction Evidence

| Activity | Result |
|---|---|
| Email opened | TBD |
| URL clicked | TBD |
| Attachment opened | TBD |
| Credentials submitted | TBD |
| Reply sent | TBD |

**Assessment:** TBD

---

## 6. Scope Evidence

The investigation should determine whether the same message or indicators were observed across additional users, mailboxes, endpoints, or identities.

**Additional Recipients:** TBD

**Related Messages:** TBD

**Related Authentication Activity:** TBD

**Related Endpoint Activity:** TBD

**Known Account Compromise:** TBD

---

## 7. Response Evidence

Potential response actions:

- Email quarantined or removed
- Sender/domain blocked
- Malicious URL blocked
- Attachment blocked or removed
- Credentials reset
- Active sessions revoked
- Endpoint investigated
- Additional recipients notified

**Actions Performed:** TBD

---

## 8. Validation Evidence

Post-response validation should confirm:

- Malicious email is no longer accessible
- Malicious indicators are blocked
- Additional recipients are no longer exposed
- No suspicious authentication continues
- No endpoint compromise is identified
- Compromised credentials are remediated when applicable

**Validation Result:** TBD

---

## 9. Evidence Limitations

The investigation should document any unavailable or incomplete telemetry.

Examples:

- Email headers unavailable
- Endpoint telemetry unavailable
- Identity telemetry unavailable
- URL click telemetry unavailable
- Attachment analysis unavailable
- Threat intelligence unavailable

**Current Limitations:** TBD

---

## 10. Analyst Assessment

### Observed Evidence

TBD

### Analyst Assessment

TBD

### Inference

TBD

### Investigation Limitations

TBD

Conclusions should be based on observed evidence and should not treat unverified assumptions as confirmed findings.

---

## 11. MITRE ATT&CK Evidence

Potential techniques:

- T1566 — Phishing
- T1566.001 — Spearphishing Attachment
- T1566.002 — Spearphishing Link
- T1566.003 — Spearphishing via Service
- T1078 — Valid Accounts, if credential compromise is confirmed

**Final Mapping:** TBD

---

## 12. Case References

- [Case Record](case.md)
- [Investigation Timeline](timeline.md)
