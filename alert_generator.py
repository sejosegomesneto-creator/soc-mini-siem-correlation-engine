import json
from datetime import datetime

def generate_alert(ip, attempts, severity):
    alert = {
        "alert_type": "Correlated Suspicious Activity",
        "source_ip": ip,
        "ssh_failed_attempts": attempts,
        "severity": severity,
        "mitre": {
            "technique_id": "T1110",
            "technique_name": "Brute Force",
            "tactic": "Credential Access"
        },
        "timestamp": datetime.now().isoformat(),
        "recommended_action": [
            "Investigar origem do IP",
            "Validar se houve bloqueio no firewall",
            "Considerar bloqueio/banimento automático (fail2ban/firewall)"
        ]
    }

    filename = f"alert_{ip.replace('.', '_')}.json"
    with open(filename, "w") as f:
        json.dump(alert, f, indent=4)

    print(f"[ALERT GENERATED] {filename}")
