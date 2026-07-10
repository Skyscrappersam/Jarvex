from app.providers.provider_manager import register
from app.api.gemini_client import GeminiClient


class GeminiProvider:

    name = "Gemini"

    def __init__(self):

        self.client = GeminiClient()

    def ask(self, prompt):

        return self.client.ask(prompt)


register(
    "gemini",
    GeminiProvider()
)