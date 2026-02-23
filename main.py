import re
from collections import defaultdict
from alert_generator import generate_alert

AUTH_LOG = "logs/auth.log"
FIREWALL_LOG = "logs/firewall.log"

FAILED_PATTERN = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

def parse_auth_log():
    attempts = defaultdict(int)
    with open(AUTH_LOG, "r") as f:
        for line in f:
            match = FAILED_PATTERN.search(line)
            if match:
                ip = match.group(1)
                attempts[ip] += 1
    return attempts

def parse_firewall_log():
    blocked_ips = set()
    with open(FIREWALL_LOG, "r") as f:
        for line in f:
            if line.startswith("BLOCK"):
                ip = line.split()[1]
                blocked_ips.add(ip)
    return blocked_ips

def correlate():
    ssh_attempts = parse_auth_log()
    blocked_ips = parse_firewall_log()

    for ip, count in ssh_attempts.items():
        # correlação: muitas falhas + IP bloqueado
        if count >= 5 and ip in blocked_ips:
            generate_alert(ip, count, severity="High")
        elif count >= 5:
            generate_alert(ip, count, severity="Medium")

if __name__ == "__main__":
    print("=== MINI SIEM - CORRELATION ENGINE ===")
    correlate()
