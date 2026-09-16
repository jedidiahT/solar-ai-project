import csv
import os

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not quite! Enter whole figures please!")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Not quite! Please enter correct format please!")

def greet_technician(name, city):
    print(f"Welcome to the Solar AI Diagnostics System")
    print(f"Technician: {name}")
    print(f"Location: {city}")

name = input("Enter your name: ")
city = input("Enter your location: ")

greet_technician(name, city)

def calculate_system_wattage(panels, wattage_per_panel):
    total = panels * wattage_per_panel
    return total

result = calculate_system_wattage(16, 550)
print(f"Total system wattage: {result}watts")

def solar_report(client_name, panels, wattage, battery_voltage):
    total_wattage = panels * wattage
    system_ok = battery_voltage > 47.5
    print(f"Client: {client_name}")
    print(f"Total System Wattage: {total_wattage }W")
    print(f"Battery Voltage: {battery_voltage}V")
    if battery_voltage > 50:
        print("System Status: Medium/Heavy Loads Acceptable.")
    elif battery_voltage > 47.5:
        print("System Status: Consider lowering Battery load for longer backup.")
    else:
        print("Warning: Battery voltage low. Lower load count to only essentials") 
       

session_clients = []
while True:
    client_name = input("Enter client name (or 'quit' to exit): ")
    if client_name == "quit":

        print(f"\nDone for today! Clients attended to this session: {len(session_clients)}")
        for client in session_clients:
            print(f" - {client['name']} | Panels: {client['panels']} | Wattage: {client['wattage']}W | Voltage: {client['battery_voltage']}V")

        file_exists = os.path.exists("session_log.csv")
        with open("session_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Panels", "Wattage", "Battery Voltage"])
            for client in session_clients:
                writer.writerow([client['name'], client['panels'], client['wattage'], client['battery_voltage']])
        print("Session saved to session_log.csv!")
        break
    panels = get_valid_int("Enter number of panels: ")
    wattage = get_valid_int("Enter panel wattage: ")
    battery_voltage = get_valid_float("Enter battery voltage: ")
    solar_report(client_name, panels, wattage, battery_voltage)
    session_clients.append({
        "name": client_name,
        "panels": panels,
        "wattage": wattage,
        "battery_voltage": battery_voltage
    })

