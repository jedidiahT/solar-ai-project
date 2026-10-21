import csv

follow_ups = 0
flagged_clients = set()

with open("job_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        diagnosis = row[6]
        if diagnosis != "Battery voltage looks great!":
            print(f"Follow up: {row[0]} - {diagnosis}")
            follow_ups = follow_ups + 1
            flagged_clients.add(row[0])

print(f"Jobs needing follow-up: {follow_ups}")
print(f"Unique clients to call: {len(flagged_clients)}")