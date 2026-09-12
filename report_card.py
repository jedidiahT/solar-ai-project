#A BRIEF REPORT CARD FOR SYSTEM MAINTENANCE #55
city = "Mutare"
country = "Zimbabwe"
client_name = "Mr. D. Simon"
date = "2nd of June, 2026"
system_setup = "48V Home Backup (10.24kWH Battery Storage, 16kW 48V Sunsynk Inverter, 14*700watts mono solar panels)"
battery_voltage = 52.2
system_battery_voltage_ok = battery_voltage > 47
nominal_charge_current = 19.6
charge_current_ok = nominal_charge_current < 15
nominal_discharge_current = 205.11
discharge_current = nominal_discharge_current < 150

print(f"Date Of Visit: {date}")
print(f"Location: {city}, {country}")
print(f"Client Name: {client_name}")
print(f"Client Setup: {system_setup}")
print(f"Battery Voltage: {battery_voltage}V")
print(f"Battery Status OK: {system_battery_voltage_ok}")
print(f"Charge Current: {nominal_charge_current}A")
print(f"Charge Status OK: {charge_current_ok}")
print(f"Discharge Current {nominal_discharge_current}A")
print(f"Discharge Status OK: {discharge_current}")
print(type(battery_voltage))
print(type(system_setup))
print(type(system_battery_voltage_ok))
