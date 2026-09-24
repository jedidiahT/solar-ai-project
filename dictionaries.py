client = {
    "name": "Mr. Dube",
    "panels":12,
    "wattage": 700,
    "battery_voltage": 52.4
}

print(f"Client {client['name']} has {client['panels']} panels and {client['battery_voltage']} on his battery")

session_clients = [
    {"name": "Mr. Dube", "panels": 12, "wattage": 700, "battery_voltage": 47.5},
     {"name": "Wattle Company", "panels": 80, "wattage": 700, "battery_voltage": 49.1},
     {"name": "John", "panels": 16, "wattage": 450, "battery_voltage": 53.3},
]

for clients in session_clients:
    print(f"Client: {clients['name']} | Panels: {clients['panels']} | Voltage: {clients['battery_voltage']}V")