INTENTS = {
    "open_browser": [
        "open chrome",
        "launch chrome",
        "start chrome",
        "open browser",
        "launch browser",
        "start browser",
        "google chrome",
        "browse internet"
    ],

    "open_camera": [
        "open camera",
        "start camera",
        "launch camera",
        "camera",
        "webcam"
    ],

    "open_notepad": [
        "open notepad",
        "launch notepad",
        "start notepad"
    ],

    "open_calculator": [
        "open calculator",
        "calculator",
        "calc",
        "start calculator"
    ],

    "open_vscode": [
        "open vscode",
        "open vs code",
        "launch vscode",
        "visual studio code"
    ]
}


def detect_intent(text):

    text = text.lower()

    for intent, phrases in INTENTS.items():

        for phrase in phrases:

            if phrase in text:
                return intent

    return None