from app.core.ai_engine import AIEngine

# Services
from app.services.automation_service import execute_command
from app.services.weather_service import get_weather
from app.services.internet_service import search_web

# Memory
from app.memory.memory_manager import (
    remember,
    recall,
    forget,
    load_memory
)

# Intent Detection
from app.core.intent_router import get_command

# Date & Time
from app.datetime_utils import (
    get_current_date,
    get_current_time,
    get_current_datetime
)

# AI Engine
ai = AIEngine()


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
    "gold",
    "share market"
]


# =====================================================
# Normal Processing
# =====================================================

def process_command(user):

    user = user.strip()
    user_lower = user.lower()

    # ==========================
    # Date & Time
    # ==========================

    if "date and time" in user_lower:
        return get_current_datetime()

    if user_lower == "date" or "current date" in user_lower:
        return get_current_date()

    if user_lower == "time" or "current time" in user_lower:
        return get_current_time()

    # ==========================
    # Weather
    # ==========================

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

    # ==========================
    # Memory
    # ==========================

    if user_lower.startswith("remember"):

        text = user[9:].strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(
                key.strip().lower(),
                value.strip()
            )

            return (
                f"🧠 Okay! I'll remember that "
                f"{key.strip()} is {value.strip()}."
            )

        return (
            "Please say something like:\n"
            "Remember favorite color is blue."
        )

    if (
        user_lower.startswith("what is")
        or user_lower.startswith("what's")
    ):

        if user_lower.startswith("what is"):
            key = user[7:].strip().lower()
        else:
            key = user[6:].strip().lower()

        value = recall(key)

        if value:
            return f"🧠 {key.title()} is {value}."

    if user_lower.startswith("forget"):

        key = user[6:].strip().lower()

        forget(key)

        return f"🗑️ I forgot '{key}'."

    if user_lower == "show memory":

        memory = load_memory()

        if not memory:
            return "🧠 My memory is empty."

        response = "🧠 Here's what I remember:\n\n"

        for key, value in memory.items():
            response += f"• {key.title()} : {value}\n"

        return response

    # ==========================
    # Intent Detection
    # ==========================

    intent_command = get_command(user)

    if intent_command:

        result = execute_command(intent_command)

        if result:
            return result

    # ==========================
    # Automation
    # ==========================

    result = execute_command(user)

    if result:
        return result

    # ==========================
    # Internet Search
    # ==========================

    if any(keyword in user_lower for keyword in internet_keywords):
        return search_web(user)

    # ==========================
    # AI
    # ==========================

    return ai.ask(user)


# =====================================================
# Streaming Processing
# =====================================================

def process_command_stream(user):

    user = user.strip()
    user_lower = user.lower()

    # ==========================
    # Date & Time
    # ==========================

    if "date and time" in user_lower:
        yield get_current_datetime()
        return

    if user_lower == "date" or "current date" in user_lower:
        yield get_current_date()
        return

    if user_lower == "time" or "current time" in user_lower:
        yield get_current_time()
        return

    # ==========================
    # Weather
    # ==========================

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
            yield "Please tell me the city name."
            return

        yield get_weather(city)
        return

    # ==========================
    # Memory
    # ==========================

    if user_lower.startswith("remember"):

        text = user[9:].strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(
                key.strip().lower(),
                value.strip()
            )

            yield (
                f"🧠 Okay! I'll remember that "
                f"{key.strip()} is {value.strip()}."
            )
            return

        yield (
            "Please say something like:\n"
            "Remember favorite color is blue."
        )
        return

    if (
        user_lower.startswith("what is")
        or user_lower.startswith("what's")
    ):

        if user_lower.startswith("what is"):
            key = user[7:].strip().lower()
        else:
            key = user[6:].strip().lower()

        value = recall(key)

        if value:
            yield f"🧠 {key.title()} is {value}."
            return

    if user_lower.startswith("forget"):

        key = user[6:].strip().lower()

        forget(key)

        yield f"🗑️ I forgot '{key}'."
        return

    if user_lower == "show memory":

        memory = load_memory()

        if not memory:
            yield "🧠 My memory is empty."
            return

        response = "🧠 Here's what I remember:\n\n"

        for key, value in memory.items():
            response += f"• {key.title()} : {value}\n"

        yield response
        return

    # ==========================
    # Intent Detection
    # ==========================

    intent_command = get_command(user)

    if intent_command:

        result = execute_command(intent_command)

        if result:
            yield result
            return

    # ==========================
    # Automation
    # ==========================

    result = execute_command(user)

    if result:
        yield result
        return

    # ==========================
    # Internet Search
    # ==========================

    if any(keyword in user_lower for keyword in internet_keywords):
        yield search_web(user)
        return

    # ==========================
    # AI Streaming
    # ==========================

    if hasattr(ai, "stream"):

        for chunk in ai.stream(user):
            yield chunk

    else:
        yield ai.ask(user)