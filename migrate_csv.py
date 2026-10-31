import csv
import sqlite3
from functions import DB_NAME, init_db

init_db()
connection = sqlite3.connect(DB_NAME)

with open("job_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        connection.execute(
            "INSERT INTO jobs (client, panels, total_wattage, battery_voltage, system_voltage, battery_type, diagnosis, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (row[0], int(row[1]), int(row[2]), float(row[3]), int(row[4]), row[5], row[6], row[7])
        )

connection.commit()
connection.close()
print("Migration Done! Database updated!")