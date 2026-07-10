import importlib
import pkgutil

PLUGINS = []


def register(plugin):
    PLUGINS.append(plugin)


def load_plugins():

    import app.plugins

    for _, module_name, _ in pkgutil.iter_modules(
        app.plugins.__path__
    ):

        if module_name == "plugin_manager":
            continue

        importlib.import_module(
            f"app.plugins.{module_name}"
        )


def get_plugins():
    return PLUGINS