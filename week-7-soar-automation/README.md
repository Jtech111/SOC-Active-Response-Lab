# Week 7 — SOAR Alert Triage Automation

## Objective
Automate SOC alert triage end to end — ingest an alert queue, classify each
IP, enrich external IPs against threat intelligence, and auto-block confirmed
malicious infrastructure with zero analyst intervention.

## Tools Used
- Python 3
- VirusTotal API v3
- Environment-variable credential handling
- Automated block lists

## Triage Logic (in order)
1. Is the IP private? -> route to SIEM log investigation (VirusTotal is blind to internal IPs)
2. Is the IP already on the block list? -> flag as REPEAT OFFENDER, fast-track
3. Otherwise -> enrich via VirusTotal across 70+ engines
4. MALICIOUS -> auto-block + log; SUSPICIOUS -> flag for investigation; CLEAN -> monitor
5. Every decision written to a timestamped triage report

## Key Concepts Demonstrated
- Threat memory: repeat offenders blocked without re-querying external APIs
- Defensive coding: .get() defaults prevent crashes on malformed API responses
- Secure credentials: API key pulled from OS environment, never hardcoded

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing (primary enrichment use case)
