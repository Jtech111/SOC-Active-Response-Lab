# Week 2 — Splunk Cloud Detection Engineering & SPL

## Objective
Ship live Linux authentication logs to Splunk Cloud via a custom Python HEC pipeline, then author SPL detection rules from scratch to automatically score and classify brute-force threats.

## Tools Used
- Splunk Cloud (Search Processing Language / SPL)
- Python 3 (HTTP Event Collector pipeline)
- Ubuntu Server 24.04 (log source)
- auth.log (raw log data)

## What I Built
- Engineered a Python script reading auth.log and shipping every line to Splunk Cloud via authenticated HEC REST API call
- Bypassed native Splunk agent limitations on ARM64 hardware using direct API ingestion
- Authored SPL detection rule detecting SSH brute force, extracting attacker IPs via regex, counting attempts, and auto-scoring threat severity

## Core SPL Detection Rule
```spl
index=main sourcetype=linux_secure "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count as failed_attempts by src_ip
| where failed_attempts > 5
| eval threat_level=if(failed_attempts>15,"HIGH","MEDIUM")
| sort -failed_attempts
```

## Key Outcome
Zero manual triage required. Any IP crossing the threshold automatically receives a HIGH or MEDIUM threat score and surfaces at the top of the detection queue.

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing
