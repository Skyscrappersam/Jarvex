from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found.")
    exit()

client = genai.Client(api_key=api_key)

print("\n===== Available Models =====\n")

try:
    for model in client.models.list():
        print(model.name)

except Exception as e:
    print("\n❌ Error:")
    print(e)