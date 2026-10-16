import csv

client_count = 0

with open("session_log.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"Visited: {row[0]}")
        client_count = client_count + 1

print (f"Total clients attended: {client_count}")        

