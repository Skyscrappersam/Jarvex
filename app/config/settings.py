import json
import os


SETTINGS_FILE = "settings.json"


DEFAULT_SETTINGS = {
    "theme": "dark",
    "voice": True
}


def load_settings():

    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    try:
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)

    except Exception:
        return DEFAULT_SETTINGS.copy()


def save_settings(settings):

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)