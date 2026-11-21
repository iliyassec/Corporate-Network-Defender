import csv
from collections import Counter


def analyze_logs(file_path):

    print("\n=== CORPORATE NETWORK DEFENDER ===")
    print("Starting security log analysis...\n")

    failed_logins = Counter()
    alerts = []

    with open(file_path, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for event in reader:

            event_type = event["event_type"]
            source_ip = event["source_ip"]

            if event_type == "login_failed":
                failed_logins[source_ip] += 1

            if event_type == "port_scan":

                alerts.append({
                    "type": "PORT SCANNING",
                    "ip": source_ip,
                    "severity": "MEDIUM"
                })

    for ip, count in failed_logins.items():

        if count >= 3:

            alerts.append({
                "type": "BRUTE FORCE SUSPECTED",
                "ip": ip,
                "severity": "HIGH"
            })

    return alerts