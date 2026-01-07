import sys
import requests
from datetime import datetime

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    response = requests.get(GEOCODE_URL, params={
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })

    data = response.json()

    if "results" not in data:
        print("City not found.")
        sys.exit(1)

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"], result["country"]


def get_weather(lat, lon):
    response = requests.get(WEATHER_URL, params={
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "relative_humidity_2m",
            "wind_speed_10m",
            "wind_direction_10m"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "sunrise",
            "sunset"
        ],
        "timezone": "auto"
    })

    return response.json()


def format_time(iso_time):
    return datetime.fromisoformat(iso_time).strftime("%I:%M %p")


def main():
    if len(sys.argv) < 2:
        print("CLI usage: python3 main.py <city>")
        sys.exit(1)

    city = sys.argv[1]

    lat, lon, city_name, country = get_coordinates(city)
    data = get_weather(lat, lon)

    current = data["current"]
    daily = data["daily"]

    print(f"\n* Weather for {city_name}, {country} *")
    print("-----------------------------------------")
    print(f"Temperature: {current['temperature_2m']}°C")
    print(f"Feels Like: {current['apparent_temperature']}°C")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind: {current['wind_speed_10m']} km/h")
    print(f"High: {daily['temperature_2m_max'][0]}°C")
    print(f"Low: {daily['temperature_2m_min'][0]}°C")
    print(f"Sunrise: {format_time(daily['sunrise'][0])}")
    print(f"Sunset: {format_time(daily['sunset'][0])}")
    print()

if __name__ == "__main__":
    main()
