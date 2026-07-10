from app.providers.provider_manager import (
    get_provider
)

# Import providers so they register themselves
import app.providers.openai_provider
import app.providers.gemini_provider
import app.providers.ollama_provider


class AIEngine:

    def __init__(self):

        self.provider_name = "gemini"

    # =====================================
    # Change AI Provider
    # =====================================

    def set_provider(self, name):

        self.provider_name = name

    # =====================================
    # Normal Response
    # =====================================

    def ask(self, prompt):

        provider = get_provider(self.provider_name)

        if provider is None:
            return "No AI provider is available."

        return provider.ask(prompt)

    # =====================================
    # Streaming Response
    # =====================================

    def stream(self, prompt):

        provider = get_provider(self.provider_name)

        if provider is None:
            yield "No AI provider is available."
            return

        # If provider supports streaming
        if hasattr(provider, "stream"):

            for chunk in provider.stream(prompt):
                yield chunk

        else:

            # Fallback for providers without streaming
            yield provider.ask(prompt)