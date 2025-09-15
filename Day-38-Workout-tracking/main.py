from datetime import datetime
import requests
import os
from requests.auth import HTTPBasicAuth

GENDER ="male"
WEIGHT_KG = 68
HEIGHT_CM = 179
AGE = 18

APP_ID ="7dee38d3"
API_KEY ="4df22569469d47ced1284d7045ef9233"
Username="DheerajkrishnaT"
Password="Dheeraj@2006"

os.environ["app_id"] = APP_ID
os.environ["api_key"] = API_KEY
os.environ["USERNAME"] = Username
os.environ["PASSWORD"] = Password

DATE=datetime.now().strftime("%d/%m/%Y")
TIME=datetime.now().strftime("%H:%M:%S")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response_workout="https://api.sheety.co/16b0518436c7a1df081b66f5933de0bc/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    workout_data = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

auth = HTTPBasicAuth(Username, Password)
data_result = requests.post(response_workout, json=workout_data, auth=auth)
print(data_result.text)