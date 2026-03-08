import yaml

from alert_generator import save_alerts
from engine.correlation_engine import correlate_ssh_bruteforce, load_whitelist
from parsers.auth_parser import parse_auth_log
from parsers.firewall_parser import parse_firewall_log


def load_rules():
    with open("config/rules.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
    rules = load_rules()
    whitelist = load_whitelist("config/whitelist.txt")

    auth_events = parse_auth_log("logs/auth.log")
    blocked_ips = parse_firewall_log("logs/firewall.log")

    alerts = correlate_ssh_bruteforce(
        events=auth_events,
        blocked_ips=blocked_ips,
        rule_config=rules["ssh_bruteforce"],
        whitelist=whitelist,
    )

    if alerts:
        saved = save_alerts(alerts)
        print("[+] Alerts generated:")
        for alert in saved:
            print(alert)
    else:
        print("[-] No suspicious activity detected.")


if __name__ == "__main__":
    main()
