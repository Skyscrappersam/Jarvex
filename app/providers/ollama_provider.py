from app.providers.provider_manager import register


class OllamaProvider:

    name = "Ollama"

    def ask(self, prompt):

        return (
            "Ollama provider is not connected yet."
        )


register("ollama", OllamaProvider())