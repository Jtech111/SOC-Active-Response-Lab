# Week 1 — Wazuh SIEM Deployment & SSH Brute Force Detection

## Objective
Deploy a production-grade Wazuh SIEM from scratch, connect a live Ubuntu target agent, simulate a real SSH brute-force attack using Hydra, and investigate the attack using only raw Linux log forensics.

## Tools Used
- Wazuh 4.14.5 (Manager / Indexer / Dashboard)
- Ubuntu Server 24.04 (soc-siem + soc-target)
- Kali Linux / Hydra (attack simulation)
- Linux CLI (grep, awk, sort, uniq, tail)

## What I Built
- Deployed full Wazuh stack (manager, indexer, dashboard) on Ubuntu via all-in-one installer
- Enrolled soc-target as a live Wazuh agent sending real-time telemetry
- Fired controlled Hydra SSH brute-force campaign (20 passwords, 4 threads) against soc-target
- Wazuh auto-generated a level-10 alert mapped to MITRE ATT&CK T1110.001

## Linux Forensics Investigation (7-Point)
Without touching the SIEM, reconstructed the entire attack from raw auth.log:
1. Counted total failed login attempts
2. Identified attacker source IP
3. Ranked top attacker IPs by volume
4. Extracted targeted usernames
5. Confirmed attack start timestamp
6. Confirmed attack end timestamp
7. Verified zero successful logins — no breach

## Key Command
```bash
sudo grep "Failed password" /var/log/auth.log | grep -oP 'from \K[\d.]+' | sort | uniq -c | sort -rn | head -5
```
Extracts attacker IPs, counts attempts per IP, sorts biggest to smallest. Core brute-force triage command.

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing

## Resume Proof
Wazuh level-10 alert auto-fired and mapped to MITRE ATT&CK T1110.001. Attack volume, source IP, targeted accounts, and 9-second attack timeline reconstructed from raw logs without SIEM dependency.
