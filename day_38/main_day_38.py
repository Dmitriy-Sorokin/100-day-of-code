import requests
from datetime import datetime
import os

now = datetime.now()
now_time = str(now.strftime("%H:%M:%S"))
data_now = str(now.strftime("%d/%m/%Y"))

Application_ID = os.environ.get("Application_ID")
API_KEY = os.environ.get("API_KEY")


user_input = "swimming 10k and cycled for 40 minutes"
current_url = "https://trackapi.nutritionix.com/v2/natural/exercise"


body = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 80.5,
    "height_cm": 180.64,
    "age": 30
}

headers = {
    "x-app-id": Application_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=current_url, json=body, headers=headers)
result = response.json()["exercises"][0]
print(result)

sheety_url = "https://api.sheety.co/18ae19b46e0eb8883332528cd03f2bf1/копияMyWorkouts/workouts"

# response_sheety = requests.get(url=sheety_url)
# print(response_sheety.text)

bopst_sheety = "https://api.sheety.co/18ae19b46e0eb8883332528cd03f2bf1/копияMyWorkouts/workouts"


sheet_inputs = {
    "workout": {
        "date": data_now,
        "time": now_time,
        "exercise": result["user_input"],
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}

response_post = requests.post(url=bopst_sheety, json=sheet_inputs)
print(response_post.text)
