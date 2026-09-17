class SolarSytstem:
    def __init__(self, client_name, panels, wattage, battery_voltage):
        self.client_name = client_name
        self.panels = panels
        self.wattage = wattage
        self.battery_voltage = battery_voltage

    def total_wattage(self):
        return self.panels * self.wattage

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

#Creating two separate solar system objects
system1 = SolarSytstem("MR. DUBE", 12, 700,52.5)
system2 = SolarSytstem("Wattle Company", 80, 650, 46.7)

system1.report()
system2.report()

        

