from app.plugins.plugin_manager import register


class MemoryPlugin:

    name = "Memory"

    version = "1.0"

    description = "AI memory system."


register(MemoryPlugin())
