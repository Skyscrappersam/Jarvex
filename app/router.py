from app.assistant import ask_jarvex
from app.automation import execute_command
from app.weather import get_weather
from app.internet import search_web
from app.memory import remember, recall
from app.datetime_utils import (
    get_current_date,
    get_current_time,
    get_current_datetime
)


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


def process_command(user):

    user = user.strip()
    user_lower = user.lower()

    # ===============================
    # Date & Time
    # ===============================

    if "date and time" in user_lower:
        return get_current_datetime()

    if user_lower == "date" or "current date" in user_lower:
        return get_current_date()

    if user_lower == "time" or "current time" in user_lower:
        return get_current_time()

    # ===============================
    # Weather
    # ===============================

    if "weather" in user_lower:

        city = user_lower

        remove_words = [
            "what",
            "what is",
            "what's",
            "weather",
            "in",
            "of",
            "today",
            "current",
            "the",
            "show me",
            "tell me"
        ]

        for word in remove_words:
            city = city.replace(word, "")

        city = city.strip()

        if city == "":
            return "Please tell me the city name."

        return get_weather(city)

    # ===============================
    # Memory
    # ===============================

    if user_lower.startswith("remember"):

        text = user[9:].strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(key.strip().lower(), value.strip())

            return f"Okay! I'll remember that {key.strip()} is {value.strip()}."

        return "Please say something like: Remember favorite color is blue."

    if user_lower.startswith("what is"):

        key = user[7:].strip().lower()

        value = recall(key)

        if value:
            return f"{key.title()} is {value}."

    # ===============================
    # Automation
    # ===============================

    result = execute_command(user)

    if result:
        return result

    # ===============================
    # Internet
    # ===============================

    if any(keyword in user_lower for keyword in internet_keywords):

        result = search_web(user)

        return result

    # ===============================
    # AI Chat
    # ===============================

    return ask_jarvex(user)