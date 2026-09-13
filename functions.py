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
       

client_name = input("Enter client name: ")
panels = int(input("Enter number of panels: "))
wattage = int(input( "Enter panel wattage: "))
battery_voltage = float(input("Enter battery voltage: "))

solar_report(client_name, panels, wattage, battery_voltage)

while True:
    client_name = input("Enter client name (or 'quit' to exit): ")
    if client_name == "quit":
        break
    panels = int(input("Enter number of panels: "))
    wattage = int(input("Enter panel wattage: "))
    battery_voltage = float(input("Enter battery voltage: "))
    solar_report(client_name, panels, wattage, battery_voltage)
