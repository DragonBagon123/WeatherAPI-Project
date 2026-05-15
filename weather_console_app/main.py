import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("OWM_API_KEY")

while True:
    city = input("Enter a city name or type exit to quit: ")

    if city.lower() == "exit":
        print("Peace")
        break

    unit_choice = input("Choose units (F for Fahrenheit or C for Celsius): ")

    if unit_choice.upper() == "F":
        units = "imperial"
        symbol = "F"
    else:
        units = "metric"
        symbol = "C"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "appid": api_key,
        "q": city,
        "units": units
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 404:
            print("City not found")
            print()
            continue

        data = response.json()

        city_name = data.get("name")
        country = data.get("sys", {}).get("country")
        temperature = data.get("main", {}).get("temp")
        humidity = data.get("main", {}).get("humidity")
        wind_speed = data.get("wind", {}).get("speed")
        description = data.get("weather")[0].get("description")

        sunrise = data.get("sys", {}).get("sunrise")
        sunset = data.get("sys", {}).get("sunset")

        sunrise_time = datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")
        sunset_time = datetime.fromtimestamp(sunset).strftime("%H:%M:%S")

        print()
        print("Weather Information")
        print("-------------------")
        print("Location:", city_name + ",", country)
        print("Temperature:", str(temperature) + "°" + symbol)
        print("Weather:", description)
        print("Humidity:", str(humidity) + "%")
        print("Wind Speed:", wind_speed)
        print("Sunrise:", sunrise_time)
        print("Sunset:", sunset_time)
        print()

    except requests.exceptions.RequestException:
        print("Network error")
        print()
