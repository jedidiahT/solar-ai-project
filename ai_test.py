from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

MODEL_NAME=("gemini-3.8-flash")

prompt = ("You are a solar engineering assistant. "
        "A technician reports: battery voltage is 44.2V on a 48V system with 16 panels at 550W each. "
        "Diagnose the issue and recommend what the technician should do. "
)
response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt
)

print(response.text)