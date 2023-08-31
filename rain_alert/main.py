import requests
import numpy as np

API_KEY = "8c8930d9f5d1da7db668813f3068260d"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    'lat': "12.971599",
    'lon': "77.594566",
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

# Here we are getting data for 5 days every 3 hours
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['list'][:4]

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        print("Bring an umbrella.")
        break
