from app.core.plugin_engine import PluginEngine

engine = PluginEngine()

print("\n====== Jarvex Plugins ======\n")

for plugin in engine.list_plugins():
    print(f"Name       : {plugin.name}")
    print(f"Version    : {plugin.version}")
    print(f"Description: {plugin.description}")
    print("-" * 30)