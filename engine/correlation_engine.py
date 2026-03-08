from collections import defaultdict
from datetime import timedelta


def load_whitelist(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return {
            line.strip()
            for line in file
            if line.strip()
        }


def correlate_ssh_bruteforce(events, blocked_ips, rule_config, whitelist):
    threshold = rule_config["threshold"]
    window_seconds = rule_config["window_seconds"]
    severity_if_blocked = rule_config["severity_if_blocked"]
    severity_if_not_blocked = rule_config["severity_if_not_blocked"]

    grouped = defaultdict(list)

    for event in events:
        ip = event["source_ip"]
        if ip in whitelist:
            continue
        grouped[ip].append(event["timestamp"])

    alerts = []

    for ip, timestamps in grouped.items():
        timestamps.sort()

        for i in range(len(timestamps)):
            start_time = timestamps[i]
            end_time = start_time + timedelta(seconds=window_seconds)

            count = sum(1 for ts in timestamps if start_time <= ts <= end_time)

            if count >= threshold:
                firewall_blocked = ip in blocked_ips
                severity = severity_if_blocked if firewall_blocked else severity_if_not_blocked

                alerts.append({
                    "alert_type": "Correlated Suspicious Activity",
                    "rule_name": "ssh_bruteforce_correlation",
                    "source_ip": ip,
                    "ssh_failed_attempts": count,
                    "time_window_seconds": window_seconds,
                    "firewall_blocked": firewall_blocked,
                    "severity": severity,
                    "mitre": {
                        "technique_id": "T1110",
                        "technique_name": "Brute Force",
                        "tactic": "Credential Access"
                    }
                })
                break

    return alerts
