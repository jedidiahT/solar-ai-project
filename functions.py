import csv
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.8-flash")

class SolarSystem:
    def __init__(self, client_name, panels, wattage, battery_voltage):
        self.client_name = client_name
        self.panels = panels
        self.wattage = wattage
        self.battery_voltage = battery_voltage

    def total_wattage(self):
        return self.panels * self.wattage

    def ai_diagnose(self):
        prompt = (
            f"You are a solar engineering assistant. "
            f"System: {self.panels} panels at {self.wattage}W each. "
            f"Battery voltage: {self.battery_voltage}V on a 48V system. "
            f"Total wattage: {self.total_wattage()}W. "
            F"Provide a brief diagnosis and recommendation in 3 sentences. "
        )
        response = model.generate_content(prompt)
        return response.text

    
    def diagnose(self):
        if self.battery_voltage > 52.1:
            return "Look's Great"
        elif self.battery_voltage > 48.4:
            return "Consider averaging load profile"
        else:
            return "Your battery bank has low charge left"


    def report(self):
        print(f"Client: {self.client_name}")
        print(f"Total Wattage: {self.total_wattage()}W")
        print(f"Battery Voltage: {self.battery_voltage}V")
        print(f"Diagnosis: {self.diagnose()}")
        print("-" * 40)

    def to_dict(self):
        return {
            "client": self.client_name,
            "panels": self.panels,
            "total_wattage": self.total_wattage(),
            "voltage": self.battery_voltage,
            "diagnosis": self.diagnose()
        }


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
            print(f" - {client['client']} | Panels: {client['panels']} | Wattage: {client['total_wattage']}W | Voltage: {client['voltage']}V")

        file_exists = os.path.exists("session_log.csv")
        with open("session_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Panels", "Wattage", "Battery Voltage"])
            for client in session_clients:
                writer.writerow([client['client'], client['panels'], client['total_wattage'], client['voltage']])
        print("Session saved to session_log.csv!")
        break
    panels = get_valid_int("Enter number of panels: ")
    wattage = get_valid_int("Enter panel wattage: ")
    battery_voltage = get_valid_float("Enter battery voltage: ")
    system = SolarSystem(client_name, panels, wattage, battery_voltage)
    system.report()
    print("\nAI Diagnosis:")
    print(system.ai_diagnose())
    session_clients.append(system.to_dict())

