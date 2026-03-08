import json
from datetime import datetime


def save_alerts(alerts, output_file="output/alerts.json"):
    enriched_alerts = []

    for alert in alerts:
        enriched = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            **alert
        }
        enriched_alerts.append(enriched)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(enriched_alerts, file, indent=4)

    return enriched_alerts
