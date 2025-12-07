import os 
from dotenv import load_dotenv
load_dotenv()
import requests
import datetime 

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://app.100daysofpython.dev"
POST_ENTPOINT = "/v1/nutrition/natural/exercise"
GENDER = "female"
AGE=30
HEIGHT = 155
WEIGHT = 47
SHEET_ID = os.environ.get("SHEET_ID")
SHEET_AUTH = os.environ.get("SHEET_AUTH")
## get exerciese data
user_input = input("Tell me which exercise you did? ")

data = {
    "query": user_input,
    "gender": GENDER,
    "age": AGE,
    "height": HEIGHT,
    "weight": WEIGHT
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=f"{BASE_URL}/{POST_ENTPOINT}", json=data, headers=headers)
response_data = response.json()["exercises"][0]
print(response_data)

## put data in the sheet 

sheety_endpoint = "https://api.sheety.co/69f7db387d564a87133246560a716a23/pythonProjectWorkout/workouts"

today = datetime.datetime.now()
format_time = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercies = response_data["name"]
duration = response_data["duration_min"]
calories = response_data["nf_calories"]

params = {
    "workout": {
        "date": str(format_time),
        "time": str(f"{time}"),
        "exercise": exercies, 
        "duration": duration, 
        "calories": calories
    }
}
sheet_header = {
    "Authorization" : f"Basic {SHEET_AUTH}"
}

sheety_response = requests.post(url=sheety_endpoint, json=params, headers=sheet_header)



