import requests


def get_weather(city):
    try:
        # Get latitude and longitude
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

        geo = requests.get(geo_url).json()

        if "results" not in geo:
            return "Sorry, I couldn't find that city."

        latitude = geo["results"][0]["latitude"]
        longitude = geo["results"][0]["longitude"]
        city_name = geo["results"][0]["name"]
        country = geo["results"][0]["country"]

        # Current weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        )

        weather = requests.get(weather_url).json()

        current = weather["current"]

        return (
            f"Current weather in {city_name}, {country}\n\n"
            f"🌡 Temperature: {current['temperature_2m']}°C\n"
            f"💧 Humidity: {current['relative_humidity_2m']}%\n"
            f"💨 Wind Speed: {current['wind_speed_10m']} km/h"
        )

    except Exception as e:
        return f"Weather Error:\n{e}"