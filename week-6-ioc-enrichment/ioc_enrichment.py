import requests
import sys
from datetime import datetime

API_KEY = "YOUR_KEY_HERE"

def check_ip(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]
    country = data["data"]["attributes"].get("country", "Unknown")
    owner = data["data"]["attributes"].get("as_owner", "Unknown")

    malicious  = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)
    total      = malicious + suspicious

    if malicious >= 5:
        verdict = "MALICIOUS"
    elif malicious >= 1 or suspicious >= 3:
        verdict = "SUSPICIOUS"
    else:
        verdict = "CLEAN"

    print(f"\nTarget:   {ip}")
    print(f"Country:  {country}")
    print(f"Owner:    {owner}")
    print(f"Engines:  {malicious} malicious / {suspicious} suspicious")
    print(f"VERDICT:  {verdict}\n")

check_ip(sys.argv[1])
