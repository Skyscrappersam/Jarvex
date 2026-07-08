from app.assistant import ask_jarvex
from app.voice import speak
from app.listener import listen
from app.automation import execute_command
from app.internet import search_web
from app.weather import get_weather
from app.datetime_utils import (
    get_current_date,
    get_current_time,
    get_current_datetime
)
from app.memory import remember, recall

print("=" * 60)
print("🤖 Jarvex AI Assistant")
print("Created by Suraj")
print("=" * 60)

internet_keywords = [
    "latest",
    "news",
    "live",
    "stock",
    "price",
    "score",
    "match",
    "cricket",
    "football",
    "ipl",
    "bitcoin",
    "gold price",
    "share market"
]

while True:

    print("\nChoose input mode:")
    print("1. Type")
    print("2. Speak")
    print("3. Exit")

    choice = input("Choice (1/2/3): ")

    if choice == "1":
        user = input("You: ")

    elif choice == "2":
        user = listen()

        if not user:
            print("Jarvex: I didn't hear anything.")
            speak("I didn't hear anything.")
            continue

        print("You:", user)

    elif choice == "3":
        print("Jarvex: Goodbye Suraj!")
        speak("Goodbye Suraj!")
        break

    else:
        print("Invalid choice.")
        continue

    user = user.strip()

    if user.lower() == "exit":
        print("Jarvex: Goodbye Suraj!")
        speak("Goodbye Suraj!")
        break

    user_lower = user.lower()

    # ==========================================
    # Date and Time
    # ==========================================

    if "date and time" in user_lower:
        result = get_current_datetime()
        print("\nJarvex:", result)
        speak(result)
        continue

    elif user_lower == "date" or "current date" in user_lower:
        result = get_current_date()
        print("\nJarvex:", result)
        speak(result)
        continue

    elif user_lower == "time" or "current time" in user_lower:
        result = get_current_time()
        print("\nJarvex:", result)
        speak(result)
        continue

    # ==========================================
    # Weather
    # ==========================================

    if "weather" in user_lower:

        city = user_lower

        remove_words = [
            "what",
            "what's",
            "what is",
            "weather",
            "in",
            "of",
            "today",
            "current",
            "the",
            "tell me",
            "show me"
        ]

        for word in remove_words:
            city = city.replace(word, "")

        city = city.strip()

        if city == "":
            city = input("Enter city name: ")

        result = get_weather(city)

        print("\nJarvex:")
        print(result)

        speak(result)

        continue

    # ==========================================
    # Open Applications
    # ==========================================

    result = execute_command(user)

    if result:
        print("\nJarvex:", result)
        speak(result)
        continue

    # ==========================================
    # Internet Search
    # ==========================================

    if any(keyword in user_lower for keyword in internet_keywords):

        print("\n🌐 Searching the internet...")

        result = search_web(user)

        print("\nJarvex:")
        print(result)

        speak("Here is what I found on the internet.")

        continue

    # ==========================================
    # Memory
    # ==========================================

    if user_lower.startswith("remember"):

        text = user[9:].strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(key.strip().lower(), value.strip())

            reply = f"Okay! I'll remember that {key.strip()} is {value.strip()}."

        else:

            reply = "Please say something like: Remember favorite color is blue."

        print("\nJarvex:", reply)
        speak(reply)
        continue

    if user_lower.startswith("what is"):

        key = user[7:].strip().lower()

        value = recall(key)

        if value:

            reply = f"{key.title()} is {value}."

            print("\nJarvex:", reply)
            speak(reply)
            continue

    # ==========================================
    # AI Chat
    # ==========================================

    reply = ask_jarvex(user)

    print("\nJarvex:")
    print(reply)

    speak(reply)