from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models_to_try = [
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
]

for model in models_to_try:
    print(f"\nTrying: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Reply with exactly: Jarvex is working!"
        )

        print(f"✅ SUCCESS using {model}")
        print(response.text)
        break

    except Exception as e:
        print(f"❌ {e}")