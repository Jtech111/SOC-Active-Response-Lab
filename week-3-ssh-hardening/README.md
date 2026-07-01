# Week 3 — Three-Layer SSH Hardening & Defensive Controls

## Objective
Deploy a three-layer defensive stack against SSH brute force attacks and confirm its effectiveness by running a live Hydra attack and observing it get cut off mid-run.

## Tools Used
- fail2ban (automated IP banning)
- sshd_config (SSH daemon hardening)
- UFW (Uncomplicated Firewall)
- Hydra (attack validation)

## The Three Layers

### Layer 1 — fail2ban
Monitors auth.log in real time. Automatically bans any IP with 5+ failed SSH attempts within a detection window. Ban confirmed by observing Hydra connections refused mid-attack.

### Layer 2 — sshd_config Hardening
Reduces maximum attempts per connection from default 6 to 3. Eliminates root login entirely — even if an attacker guesses the password, root access is denied at the protocol level.

### Layer 3 — UFW Firewall
```bash
sudo ufw default deny incoming
sudo ufw allow from 192.168.64.0/24 to any port 22
sudo ufw enable
```
Deny-all default policy. SSH access explicitly allowed only from the authorized lab subnet. Any external IP attempting to reach port 22 is dropped at the firewall before it even reaches SSH.

## Proof of Effectiveness
Fired Hydra attack after all three layers were deployed. Observed:
- Hydra worker threads dying mid-run with "too many connection errors"
- fail2ban log showing "Ban 192.168.64.9" in real time
- Connection refused on subsequent attempts

## MITRE ATT&CK Mapping
T1110.001 — Brute Force: Password Guessing (mitigated)
M1036 — Account Use Policies
M1030 — Network Segmentation
