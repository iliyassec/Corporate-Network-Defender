import sqlite3


DB_NAME = "corporate_defender.db"


def create_database():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            threat_type TEXT NOT NULL,

            source_ip TEXT NOT NULL,

            severity TEXT NOT NULL,

            status TEXT DEFAULT 'NEW',

            detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()

    print("[DATABASE] Database initialized successfully.")


def save_incident(threat_type, source_ip, severity):

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO incidents
        (threat_type, source_ip, severity)

        VALUES (?, ?, ?)
    """, (threat_type, source_ip, severity))

    connection.commit()

    connection.close()

    print(f"[DATABASE] Incident saved: {threat_type}")


def get_incidents():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, threat_type, source_ip,
               severity, status, detected_at
        FROM incidents
        ORDER BY id DESC
    """)

    incidents = cursor.fetchall()

    connection.close()

    return incidents