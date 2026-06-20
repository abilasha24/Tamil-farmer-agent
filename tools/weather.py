import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city="Jaffna"):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ta"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        return {
            "city": city,
            "temperature": temp,
            "humidity": humidity,
            "description": description
        }
    else:
        return {"error": "Weather data கிடைக்கல"}

if __name__ == "__main__":
    weather = get_weather("Jaffna")
    print(weather)