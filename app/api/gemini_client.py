from google import genai

from app.api.api_keys import get_gemini_key


class GeminiClient:

    def __init__(self):

        api_key = get_gemini_key()

        if not api_key:
            raise ValueError(
                "❌ GEMINI_API_KEY not found in .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        # Working model alias
        self.model = "gemini-flash-latest"

    def ask(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if hasattr(response, "text") and response.text:
                return response.text

            return "Sorry, Gemini returned an empty response."

        except Exception as e:

            error = str(e)

            if "RESOURCE_EXHAUSTED" in error:
                return (
                    "⚠️ Gemini quota exceeded.\n"
                    "Please wait a minute and try again."
                )

            elif "NOT_FOUND" in error:
                return (
                    "⚠️ Gemini model not found."
                )

            elif "PERMISSION_DENIED" in error:
                return (
                    "⚠️ Invalid Gemini API Key."
                )

            elif "UNAUTHENTICATED" in error:
                return (
                    "⚠️ Authentication failed. Check your API key."
                )

            return f"❌ Gemini Error:\n{error}"