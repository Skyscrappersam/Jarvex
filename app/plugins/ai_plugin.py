from app.plugins.plugin_manager import register


class AIPlugin:

    name = "AI"

    version = "1.0"

    description = "Natural language AI."


register(AIPlugin())