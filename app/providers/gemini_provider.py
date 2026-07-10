from app.providers.provider_manager import register


class GeminiProvider:

    name = "Gemini"

    def ask(self, prompt):

        return (
            "Gemini provider is not connected yet."
        )


register("gemini", GeminiProvider())