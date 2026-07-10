from app.plugins.plugin_manager import register


class WeatherPlugin:

    name = "Weather"

    version = "1.0"

    description = "Provides weather information."


register(WeatherPlugin())