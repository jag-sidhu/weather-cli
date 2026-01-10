# weather_cli

A command-line weather app in Python that fetches real-time weather data using the Open-Meteo API and provides a clean, readable forecast for any city.
No API keys are required. This project demonstrates API integration, CLI design and basic Python programming.

__Features:__
- Get current weather for any city:
- Temperature
- Feels-like temperature
- Humidity
- Wind speed
- Daily high and low temperatures
- Daily sunrise and sunset times

* Handles errors gracefully (such as invalid city input)

Clean, readable CLI output -> example:

    Weather for Vancouver, Canada
    ------------------------------------------
    Temperature: 4.4°C
    Feels Like: 2.0°C
    Humidity: 88%
    Wind: 4.7 km/h
    High: 5.5°C
    Low: 2.7°C
    Sunrise: 08:06 AM
    Sunset: 04:30 PM

__Requirements:__
- Python3
- Requests library (pip3 install requests)

__Usage:__
Run this program in terminal using the following command: python3 main.py <city>
-> python3 main.py Vancouver

__Potential Improvements:__
- Add hourly forecast
- Include air quality index or UV index
- Multi-city comparison
- Save results to file or JSON
- Upgrade from CLI to a web app with more interactive features