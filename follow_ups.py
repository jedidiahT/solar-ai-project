import csv

follow_ups = 0

with open("job_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        diagnosis = row[6]
        if diagnosis != "Battery voltage looks great!":
            print(f"Follow up: {row[0]} - {diagnosis}")
            follow_ups = follow_ups + 1

print(f"Clients needing follow-up: {follow_ups}")