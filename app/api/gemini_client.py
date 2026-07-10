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

        self.model = "gemini-flash-latest"

    # ===================================
    # Normal Response
    # ===================================

    def ask(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            if response.text:
                return response.text

            return "Sorry, Gemini returned an empty response."

        except Exception as e:

            return f"❌ Gemini Error:\n{e}"

    # ===================================
    # Streaming Response
    # ===================================

    def stream(self, prompt):

        try:

            stream = self.client.models.generate_content_stream(
                model=self.model,
                contents=prompt
            )

            for chunk in stream:

                if hasattr(chunk, "text") and chunk.text:
                    yield chunk.text

        except Exception as e:

            yield f"\n❌ Gemini Error:\n{e}"