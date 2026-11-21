print("================================")
print(" CORPORATE NETWORK DEFENDER")
print("================================")

print("System status: RUNNING")
print("Security monitoring: INITIALIZED")
print("Welcome to your first SOC project!")

from detector.log_analyzer import analyze_logs
from detector.alert_manager import show_alerts

from database.database import (
    create_database,
    save_incident,
    get_incidents
)


def main():

    file_path = "logs/sample_events.csv"

    # Initialize database
    create_database()

    # Analyze security logs
    alerts = analyze_logs(file_path)

    # Show alerts
    show_alerts(alerts)

    # Save incidents
    for alert in alerts:

        save_incident(
            alert["type"],
            alert["ip"],
            alert["severity"]
        )

    # Display saved incidents
    print("\n=== INCIDENT DATABASE ===")

    incidents = get_incidents()

    for incident in incidents:

        print(incident)


if __name__ == "__main__":
    main()