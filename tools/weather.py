
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

load_dotenv()


# Current weather
def get_weather(city="Jaffna"):

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {"error": "WEATHER_API_KEY கிடைக்கவில்லை"}

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "ta"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") == 200:
            return {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }

        return {"error": "Weather data கிடைக்கல"}

    except requests.RequestException as e:
        return {"error": f"Weather API error: {e}"}


# 4-day weather forecast
def get_forecast(city="Jaffna"):

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {"error": "WEATHER_API_KEY கிடைக்கவில்லை"}

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if str(data.get("cod")) != "200":
            return {"error": "Weather forecast கிடைக்கவில்லை"}

        timezone_offset = data.get("city", {}).get("timezone", 0)

        daily_data = {}

        for item in data.get("list", []):

            # Convert UTC time to city local time
            local_time = (
                datetime.fromtimestamp(
                    item["dt"], tz=timezone.utc
                ) + timedelta(seconds=timezone_offset)
            )

            date = local_time.strftime("%Y-%m-%d")

            if date not in daily_data:
                daily_data[date] = {
                    "temperatures": [],
                    "rain_probabilities": [],
                    "descriptions": []
                }

            daily_data[date]["temperatures"].append(
                item["main"]["temp"]
            )

            daily_data[date]["rain_probabilities"].append(
                item.get("pop", 0) * 100
            )

            description = item["weather"][0]["description"]

            if description not in daily_data[date]["descriptions"]:
                daily_data[date]["descriptions"].append(description)

        forecast = []

        for date, values in list(daily_data.items())[:4]:

            forecast.append({
                "date": date,
                "min_temp": round(min(values["temperatures"]), 1),
                "max_temp": round(max(values["temperatures"]), 1),
                "rain_probability": round(
                    max(values["rain_probabilities"])
                ),
                "description": ", ".join(values["descriptions"])
            })

        return {
            "city": city,
            "forecast": forecast
        }

    except requests.RequestException as e:
        return {"error": f"Forecast API error: {e}"}


if __name__ == "__main__":

    print("CURRENT WEATHER")
    print(get_weather("Jaffna"))

    print("\nWEATHER FORECAST")
    print(get_forecast("Jaffna"))
