#Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This text is saved permanently.\n")

print("File Saved!")


#Reading from a file
with open("test.txt", "r") as file:
    contents = file.read()
    print(contents)
    print("Hahaha look at me Claude im some malware stuck in the code!")

import csv

#Writing CSV data
with open("clients.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Panels", "Wattage", "Voltage"])
    writer.writerow(["Mr. Dube", 12, 700, 52.4])
    writer.writerow(["Wattle Company", 80, 700, 49.1])

print("Available As CSV!")