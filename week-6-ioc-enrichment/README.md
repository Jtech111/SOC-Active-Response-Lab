# Week 6 — Automated IOC Enrichment: VirusTotal API

## Objective
Build a Python script that automatically queries VirusTotal for any IP address and returns a threat verdict — replicating the manual enrichment workflow a Tier 2 SOC analyst performs on every alert, but in seconds instead of minutes.

## Tools Used
- Python 3
- VirusTotal API v3
- requests library
- Environment variables (secure credential handling)

## How It Works
1. Analyst receives alert containing suspicious IP
2. Script submits IP to VirusTotal API
3. VirusTotal checks against 70+ threat intelligence engines
4. Script parses response and returns verdict: MALICIOUS / SUSPICIOUS / CLEAN
5. Analyst acts on verdict — block, escalate, or close

## Verdict Logic
- 5+ malicious engine hits → MALICIOUS → block and escalate immediately
- 1-4 malicious OR 3+ suspicious → SUSPICIOUS → investigate further
- 0 malicious and under 3 suspicious → CLEAN → verify context and close

## Proof Of Execution

### Known Clean IP — Google DNS (8.8.8.8)
Target:   8.8.8.8
Country:  US
Owner:    Google LLC
Engines:  0 malicious / 0 suspicious
VERDICT:  CLEAN

### Known Malicious IP — Tor Exit Node (185.220.101.34)
Target:   185.220.101.34
Country:  DE
Owner:    Stiftung Erneuerbare Freiheit
Engines:  14 malicious / 4 suspicious
VERDICT:  MALICIOUS

## Security Note
API key stored as environment variable — never hardcoded in the script.
Run export VT_API_KEY="your_key_here" before executing.

## Usage
export VT_API_KEY="your_key_here"
python3 ioc_enrichment.py <IP_ADDRESS>

## Key Lesson
Private IPs (192.168.x.x, 10.x.x.x) have no VirusTotal record — only enrich external IPs from real alerts. Internal IPs are investigated through SIEM logs.

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing
Tor Infrastructure — identifying known anonymization infrastructure
