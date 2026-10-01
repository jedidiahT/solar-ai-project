from flask import Flask, request, jsonify

from functions import SolarSystem

app = Flask(__name__)

@app.route("/")
def home():
    return "Solar AI Diagnostics System is running!"

@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    return {"message": "recieved", "client": data["client_name"]}

if __name__ == "__main__":
    app.run(debug=True)
