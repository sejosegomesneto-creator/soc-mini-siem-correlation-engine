import re

FIREWALL_REGEX = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
)


def parse_firewall_log(file_path):
    blocked_ips = set()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "block" not in line.lower() and "deny" not in line.lower():
                continue

            match = FIREWALL_REGEX.search(line)
            if match:
                blocked_ips.add(match.group("ip"))

    return blocked_ips
