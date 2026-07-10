from app.plugins.plugin_manager import (
    load_plugins,
    get_plugins
)


class PluginEngine:

    def __init__(self):

        load_plugins()

        self.plugins = get_plugins()

    def list_plugins(self):

        return self.plugins