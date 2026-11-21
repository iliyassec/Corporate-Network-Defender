def show_alerts(alerts):

    print("\n=== SECURITY ALERTS ===")

    if not alerts:
        print("No threats detected.")
        return

    for alert in alerts:

        print("\n[WARNING]")
        print("Threat:", alert["type"])
        print("Source IP:", alert["ip"])

    print("\nTotal alerts:", len(alerts))