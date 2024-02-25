import logging
import os
import requests


class service:
    API_KEY = os.environ.get("OPENWEATHER_API_KEY")
    API_URL = "https://api.openweathermap.org/data/2.5/forecast"
    INTERVALS_PER_DAY = 8

    @staticmethod
    def get_temperature(city: str, days: int) -> float:
        return service._get_forecast(city, days)["main"]["temp"]

    @staticmethod
    def will_rain(city: str, days: int) -> bool:
        return service._get_forecast(city, days)["weather"][0]["main"] == "Rain"

    @staticmethod
    def _get_forecast(city: str, days: int) -> dict:
        params = {"q": city, "appid": service.API_KEY, "units": "metric"}

        try:
            response = requests.get(service.API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == "200":
                return data["list"][(service.INTERVALS_PER_DAY * days)]
        except requests.RequestException as e:
            logging.error(f"Failed to fetch forecast data: {e}")

        raise ValueError("Failed to fetch forecast data")
