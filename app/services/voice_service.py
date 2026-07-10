import pyttsx3

def speak(text):
    engine = pyttsx3.init()   # Create a new engine every time
    engine.setProperty("rate", 170)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()