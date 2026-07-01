# Week 4 — Windows Security Event Log Analysis & Cross-Subnet Detection

## Objective
Extend the SOC lab to a Windows 11 endpoint on a separate network subnet, ship Windows Security Event logs to Splunk Cloud via PowerShell HEC pipeline, and build SPL detection for Windows failed logon patterns.

## Tools Used
- Windows 11 ARM64 (Parallels, 10.211.55.x subnet)
- PowerShell (HEC log shipping pipeline)
- Splunk Cloud (SPL detection)
- Wazuh Windows Agent

## Architecture
Dual-hypervisor cross-subnet setup:
- UTM subnet: 192.168.64.x (Linux VMs)
- Parallels subnet: 10.211.55.x (Windows VM)
- Both subnets feeding centralized Splunk Cloud SIEM

Mirrors enterprise segmented network architecture where endpoints on different VLANs all report to a central SIEM.

## Key Windows Event IDs
| Event ID | Meaning |
|----------|---------|
| 4624 | Successful logon |
| 4625 | Failed logon — primary brute force indicator |
| 4672 | Special privileges assigned — admin logon |
| 4720 | New user account created |
| 4732 | User added to security group |

## Logon Types
| Type | Meaning |
|------|---------|
| Type 3 | Network logon (remote file access, SMB) |
| Type 10 | RemoteInteractive — RDP session |

## SPL Detection Rule
```spl
index=main EventCode=4625
| stats count as failed_logons by src_ip, Account_Name
| where failed_logons > 5
| eval threat_level=if(failed_logons>15,"HIGH","MEDIUM")
| sort -failed_logons
```

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing
T1078 — Valid Accounts (detection via 4624 after 4625 pattern)
