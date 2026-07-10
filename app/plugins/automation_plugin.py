from app.plugins.plugin_manager import register


class AutomationPlugin:

    name = "Automation"

    version = "1.0"

    description = "Desktop automation."


register(AutomationPlugin())