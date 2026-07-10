from app.providers.provider_manager import register
from app.api.gemini_client import GeminiClient


class GeminiProvider:

    name = "Gemini"

    def __init__(self):

        self.client = GeminiClient()

    # =====================================
    # Normal Response
    # =====================================

    def ask(self, prompt):

        return self.client.ask(prompt)

    # =====================================
    # Streaming Response
    # =====================================

    def stream(self, prompt):

        for chunk in self.client.stream(prompt):
            yield chunk


register(
    "gemini",
    GeminiProvider()
)