from flask import Flask, request, jsonify, render_template

from functions import SolarSystem, save_job

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    system = SolarSystem(
        data["client_name"],
        data["panels"],
        data["wattage"],
        data["battery_voltage"],
        data.get("system_voltage", 48),
        data.get("battery_type", "lifepo4")
        )
    result = system.to_dict()
    result["ai_diagnosis"] = system.ai_diagnose()
    save_job(system)
    return result
if __name__ == "__main__":
    app.run(debug=True)
