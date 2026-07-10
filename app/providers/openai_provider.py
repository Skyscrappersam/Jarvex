from app.providers.provider_manager import register


class OpenAIProvider:

    name = "OpenAI"

    def ask(self, prompt):

        from app.assistant import ask_jarvex

        return ask_jarvex(prompt)


register("openai", OpenAIProvider())