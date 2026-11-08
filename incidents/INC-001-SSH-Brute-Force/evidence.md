# INC-001 — Evidence Record

## Evidence Summary

This document records the evidence reviewed during the SSH brute-force investigation.

Evidence is separated from analyst conclusions to maintain an evidence-first investigation process.

---

## 1. Wazuh Detection

**Evidence Type:** SIEM Alert

**Source:** Wazuh

**Observed:**

Wazuh generated an alert associated with repeated SSH authentication failures against the monitored Linux host.

**What this demonstrates:**

The SIEM identified a repeated authentication pattern requiring analyst review.

---

## 2. Linux Authentication Logs

**Evidence Type:** Endpoint Log

**Source:** Linux SSH authentication telemetry

**Observed:**

Repeated failed SSH authentication attempts were recorded against the monitored SSH service.

**What this demonstrates:**

The authentication activity was not an isolated failed login and exhibited a repeated pattern consistent with credential-guessing activity.

---

## 3. Authentication Outcome

**Evidence Type:** Authentication Records

**Observed:**

The reviewed authentication evidence showed repeated failed authentication attempts.

**Not Observed:**

No successful attacker authentication was identified in the reviewed evidence.

**Investigation Limitation:**

This conclusion applies only to the telemetry and time period reviewed during the investigation.

---

## 4. Attack Testing

**Evidence Type:** Attack Simulation Output

**Observed:**

Automated SSH authentication attempts were generated against the monitored Linux host during controlled lab testing.

**What this demonstrates:**

The controlled test reproduced the authentication pattern observed by the SIEM and endpoint telemetry.

---

## 5. Defensive Response

**Evidence Type:** Configuration / Response Evidence

**Observed:**

Defensive controls were implemented including:

- fail2ban
- SSH configuration hardening
- UFW firewall controls

**What this demonstrates:**

The investigation progressed from detection and analysis into defensive response.

---

## 6. Post-Response Validation

**Evidence Type:** Repeat Attack Test

**Observed:**

A repeat attack was performed after defensive controls were implemented.

The documented testing showed the attack being interrupted at approximately attempt 14 after hardening compared with approximately attempt 24 during the original test.

**What this demonstrates:**

The defensive changes reduced the number of successful attack attempts before the attack was interrupted.

---

## 7. Analyst Assessment

### Confirmed

- Repeated SSH authentication failures occurred.
- The activity was consistent with automated brute-force behavior.
- Defensive controls were implemented.
- Post-response testing demonstrated improved defensive effectiveness.

### Not Observed

- Successful attacker authentication in the reviewed evidence.
- Confirmed persistence.
- Confirmed lateral movement.
- Confirmed additional affected hosts.

### Unable to Determine

The available lab telemetry does not establish whether the same source attempted authentication against systems outside the monitored environment.

---

## 8. Evidence Limitations

This investigation is based on the telemetry and controlled testing available within the lab environment.

Absence of evidence in the reviewed telemetry should not be interpreted as proof that an event could never have occurred.

---

## 9. Supporting Evidence

Supporting screenshots, logs, command output, and configuration evidence should be maintained in the repository's evidence/screenshot locations and referenced from this case when applicable.
