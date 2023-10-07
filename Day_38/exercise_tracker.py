from dotenv import load_dotenv
import os
from icecream import ic
import requests
import datetime as dt

load_dotenv()

API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ID = os.environ.get("SHEETY_ID")
TOKEN = os.environ.get("TOKEN")
GENDER = "female"
WEIGHT = round((270 * 0.45359237), 1)
HEIGHT = round((6 * 30.48), 2)
AGE = 36
EXERCISE_INPUT = input("What exercise did you do today? \n")
# EXERCISE_INPUT = "ran 3 miles"
TODAY = dt.datetime.now().strftime("%Y-%m-%d")
TIME = dt.datetime.now().strftime("%H:%M:%S")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": EXERCISE_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

tracker_url = f"https://api.sheety.co/{SHEETY_ID}/myWorkoutTracker2/workouts"

tracker_header = {
    "Authorization": TOKEN,
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
data = response.json()
output = data["exercises"]
# ic(output)
for item in output:
    workout_params = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    # ic(workout_params)
    update_sheet = requests.post(url=tracker_url, json=workout_params, headers=tracker_header)
    update_sheet.raise_for_status()
    ic(update_sheet.json())


def view_tracker():
    view_response = requests.get(url=tracker_url)
    view_response.raise_for_status()
    ic(view_response.json())

# ic(view_tracker())
