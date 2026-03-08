import re
from datetime import datetime

AUTH_REGEX = re.compile(
    r'^(?P<month>\w{3})\s+(?P<day>\d+)\s+(?P<time>\d{2}:\d{2}:\d{2}).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)'
)

CURRENT_YEAR = datetime.now().year


def parse_auth_log(file_path):
    events = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = AUTH_REGEX.search(line)
            if not match:
                continue

            try:
                timestamp = datetime.strptime(
                    f"{CURRENT_YEAR} {match.group('month')} {match.group('day')} {match.group('time')}",
                    "%Y %b %d %H:%M:%S"
                )
            except ValueError:
                continue

            events.append({
                "timestamp": timestamp,
                "source_ip": match.group("ip"),
                "raw": line.strip()
            })

    return events
