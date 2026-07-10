from app.providers.provider_manager import (
    get_provider
)

# Import providers so they register themselves
import app.providers.openai_provider
import app.providers.gemini_provider
import app.providers.ollama_provider


class AIEngine:

    def __init__(self):

        self.provider_name = "openai"

    def set_provider(self, name):

        self.provider_name = name

    def ask(self, prompt):

        provider = get_provider(self.provider_name)

        if provider is None:
            return "No AI provider is available."

        return provider.ask(prompt)