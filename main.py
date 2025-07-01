from pickle import GLOBAL
import os
import requests
from datetime import datetime

data = None

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
Sheety_token = os.environ.get("TOKEN")

#Food_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = 'https://api.sheety.co/566f608a22aeba3af72fe2153077bb2e/workout/sheet1'

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

def exercise():
    global data
    query = {
        "query": input("Tell me the exercise u did:\n")
    }

    response = requests.post(url=exercise_endpoint, json=query, headers=headers)
    response.raise_for_status()
    data = response.json()["exercises"]
    return data

exercise()
if not data:
    print("Please enter valid input")
    exercise()

today = datetime.now()
date = today.strftime("%d/%m/%y")
time = today.strftime("%H:%M:%S")
headers = {
    "Authorization": Sheety_token
}


for val in data:
    exercise_data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": val["user_input"].title(),
            "duration": f"{val["duration_min"]} min",
            "calories": val["nf_calories"]
        }
    }
    response = requests.post(url=sheety_endpoint, json=exercise_data,headers= headers)
    print(response.text)













