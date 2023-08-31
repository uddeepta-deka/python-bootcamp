import requests
from datetime import datetime

MY_LAT, MY_LNG = 13.145637669268584, 77.51471504685006
DELTA = 5
now_hour = int(datetime.now().hour)

iss_api_response = requests.get(
    url="http://api.open-notify.org/iss-now.json")
iss_api_response.raise_for_status()
sunrise_sunset_api_response = requests.get(
    url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
sunrise_sunset_api_response.raise_for_status()

current_iss_lng = float(iss_api_response.json()["iss_position"]["longitude"])
current_iss_lat = float(iss_api_response.json()["iss_position"]["latitude"])
sunrise_hour = int(sunrise_sunset_api_response.json()["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
sunset_hour = int(sunrise_sunset_api_response.json()["results"]["sunset"].split("T")[1].split(":")[0]) + 5


def iss_is_visible():
    return (sunset_hour < now_hour or now_hour < sunrise_hour) and \
           MY_LAT-DELTA < current_iss_lat < MY_LAT+DELTA \
           and MY_LNG-DELTA < current_iss_lng < MY_LNG+DELTA


if iss_is_visible():
    print("Look up! The ISS is above you in the sky")
