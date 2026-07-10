from app.core.intent_detector import detect_intent


INTENT_TO_COMMAND = {

    "open_browser": "browser",

    "open_camera": "camera",

    "open_notepad": "notepad",

    "open_calculator": "calculator",

    "open_vscode": "vs code"

}


def get_command(text):

    intent = detect_intent(text)

    if intent:

        return INTENT_TO_COMMAND[intent]

    return None