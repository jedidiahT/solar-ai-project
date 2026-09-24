import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.8-flash")

response = model.generate_content("You are a solar engineering assistant. "
                                  "A technician reports: battery voltage is 44.2V on a 48V system with 16 panels at 550W each. "
                                  "Diagnose the issue and recommend what the technician should do. "
)

print(response.text)