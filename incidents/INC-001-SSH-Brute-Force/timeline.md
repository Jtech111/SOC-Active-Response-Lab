# INC-001 — Investigation Timeline

## Timeline

| Sequence | Event | Analyst Action / Finding |
|---|---|---|
| 1 | Wazuh generated SSH authentication alert | Alert acknowledged and validated |
| 2 | Repeated failed SSH authentication observed | Activity assessed as suspicious |
| 3 | Authentication telemetry reviewed | Brute-force pattern identified |
| 4 | Source and target reviewed | Scope established against monitored Linux SSH service |
| 5 | Authentication outcomes reviewed | No successful attacker authentication identified in reviewed evidence |
| 6 | Attack activity analyzed | Activity assessed as automated SSH credential guessing |
| 7 | Defensive controls applied | fail2ban, SSH hardening, and UFW controls implemented |
| 8 | Attack repeated after hardening | Defensive effectiveness tested |
| 9 | Attack interrupted earlier | Post-response validation demonstrated improved defensive effectiveness |
| 10 | Investigation completed | Incident documented and closed |

---

## Investigation Phases

### Detection

Wazuh identified repeated failed SSH authentication activity.

### Triage

The alert was validated against Linux authentication telemetry and assessed as suspicious activity requiring investigation.

### Investigation

Authentication logs and Wazuh telemetry were reviewed to determine attack pattern, source, target, authentication outcome, and scope.

### Response

Defensive controls were applied through fail2ban, SSH configuration hardening, and UFW firewall controls.

### Validation

The attack was repeated after defensive changes to determine whether the controls reduced attack effectiveness.

### Closure

The activity was confirmed as malicious SSH brute-force behavior. No successful attacker authentication was identified in the reviewed evidence, and the defensive response was validated.
