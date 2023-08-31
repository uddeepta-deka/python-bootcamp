"""
This code takes an user input about the workout they have done and stores
relevant data in https://docs.google.com/spreadsheets/d/1De02PnddNxjqV-n_3OcLXpebvWruP7xFUFNuh2_h7vc/edit?usp=sharing
"""

import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "69"
HEIGHT_CM = "170.18"
AGE = "27"
APP_ID = "e6816ba4"
API_KEY = "3bc99736a7fc2feb60aa3e3aa19604a8"
SHEETY_BEARER_TOKEN = "jlkaeinlaxlknfoielLKDLfelkalKSe"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

sheety_add_row_endpoint = "https://api.sheety.co/9bff6130234e71994ddb2b8b752df249/myWorkouts/workouts"
sheety_endpoint_name = "workout"
today = datetime.now()

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}
for exercise in result['exercises']:
    sheet_inputs = {
        sheety_endpoint_name: {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheety_add_row_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)