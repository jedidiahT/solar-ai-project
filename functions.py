import csv
import os
import time
import sqlite3
from datetime import datetime
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.1-flash-lite"

BATTERY_PROFILES = {
    "lifepo4": {
        "name": "LiFePO4",
        "cells_per_12v": 4,
        "2_hi": 3.9,
        "upp_lmt": 3.67,
        "hlthy": 3.35,
        "cons": 3.15,
        "lw": 2.95
    },
    "lead_acid": {
        "name": "Lead-Acid",
        "cells_per_12v": 6,
        "2_hi": 2.5,
        "upp_lmt": 2.4,
        "hlthy": 2.1,
        "cons": 2.05,
        "lw": 1.95
    }
}

DB_NAME = "solar_ai.db"
def init_db():
    connection = sqlite3.connect(DB_NAME)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client TEXT,
            panels INTEGER,
            total_wattage INTEGER,
            battery_voltage REAL,
            system_voltage INTEGER,
            battery_type TEXT,
            diagnosis TEXT,
            date TEXT)
    """)
    connection.commit()
    connection.close()

class SolarSystem:
    def __init__(self, client_name, panels, wattage, battery_voltage, system_voltage=48, battery_type="lifepo4"):
        self.client_name = client_name
        self.panels = panels
        self.wattage = wattage
        self.battery_voltage = battery_voltage
        self.system_voltage = system_voltage
        self.battery_type = battery_type

    def total_wattage(self):
        return self.panels * self.wattage

    def cell_voltage(self):
        profile = BATTERY_PROFILES[self.battery_type]
        cells = (self.system_voltage / 12) * profile["cells_per_12v"]
        return self.battery_voltage / cells

    def ai_diagnose(self):
        prompt = (
            "You are a solar engineering assistant. "
            f"System: {self.panels} panels at {self.wattage}W each. "
            f"Battery voltage: {self.battery_voltage}V on a {self.system_voltage}V system. "
            f"Total wattage: {self.total_wattage()}W. "
            f"Battery type: {BATTERY_PROFILES[self.battery_type]['name']} "
            f"Average cell voltage: {self.cell_voltage():.2f}V. "
            f"Our rule-based diagnosis says: {self.diagnose()} "
            "If you disagree with the native, rule-based diagnosis, explain why in brief. "
            "Provide a brief diagnosis of your own and recommendation in 3 sentences. "
            "Respond in plain text only. Do not use Markdown, asterisks, bullet points or headings. "
        )
        last_error = "Unknown"
        for attempt in range(2):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        http_options=types.HttpOptions(timeout=37000)
                    )
                )
                return response.text
            except Exception as error:
                last_error = type(error).__name__
                print(f"AI error details (attempt {attempt + 1}): {error}")
                time.sleep(2)
        return f"Oops! your in-depth diagnosis isn't available right now. ({last_error}). Stick with the brief for now!"
            

    
    def diagnose(self):
        cell_voltage = self.cell_voltage()
        profile = BATTERY_PROFILES[self.battery_type]

        if cell_voltage > profile["2_hi"]:
            return "Voltage reading too high. Please ensure correct reading."
        elif cell_voltage > profile["upp_lmt"]:
            return "Upper-limit threshold. Disconnect charge supply."
        elif cell_voltage > profile["hlthy"]:
            return "Battery voltage looks great!"
        elif cell_voltage > profile["cons"]:
            return "Consider lowering load profile."
        elif cell_voltage > profile["lw"]:
            return "Low charge left. Switch load to essentials only."
        else:
            return "WARNING: Battery is too low. Further use will damage the cells beyond repair!"


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
            "system_voltage": self.system_voltage,
            "diagnosis": self.diagnose()
        }

def save_job(system):
    connection = sqlite3.connect(DB_NAME)
    connection.execute(
        "INSERT INTO jobs (client, panels, total_wattage, battery_voltage, system_voltage, battery_type, diagnosis, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            system.client_name,
            system.panels,
            system.total_wattage(),
            system.battery_voltage,
            system.system_voltage,
            system.battery_type,
            system.diagnose(),
            datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    )
    connection.commit()
    connection.close()

def get_follow_ups():
    if not os.path.exists("job_log.csv"):
        return []

    flagged = []
    with open("job_log.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[6] != "Battery voltage looks great!":
                flagged.append({"client": row[0], "diagnosis": row[6], "date": row[7]})
    return flagged       

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
    print("WELCOME BACK TO YOUR JOURNAL, ENGINEER")
    print(f"Technician: {name}")
    print(f"Location: {city}")

def calculate_system_wattage(panels, wattage_per_panel):
    total = panels * wattage_per_panel
    return total


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
        print("Warning: Battery voltage low. Lower load count to only essentials.")

       

if __name__ == "__main__":
    name = input("Greetings Engineer: ")
    city = input("Where are you today?: ")
    greet_technician(name, city)

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

