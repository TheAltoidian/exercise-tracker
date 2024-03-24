from APIkeys import app_ID, app_Key
import requests
from datetime import datetime

exercise = input("What exercise did you do?: ")
print(exercise)
# exercise = "ran 2 miles"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": exercise
}

exercise_headers = {
    "x-app-id": app_ID,
    "x-app-key": app_Key,
    "Content-Type": "application/json",
}

response = requests.post(url=exercise_endpoint, headers=exercise_headers, json=exercise_params)
response.raise_for_status()
data = response.json()
# print(data)
# test = {'exercises': [{
#     'tag_id': 317,
#     'user_input': 'ran',
#     'duration_min': 20.01,
#     'met': 9.8,
#     'nf_calories': 228.78,
#     'photo': {
#         'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
#         'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
#         'is_user_uploaded': False
#     },
#     'compendium_code': 12050,
#     'name': 'running',
#     'description': None,
#     'benefits': None}]}
info = data["exercises"][0]
workout = info["user_input"]
duration = info["duration_min"]
calories = info["nf_calories"]
print(f"workout: {workout}, duration: {duration}, calories: {calories}")

now = datetime.now()
print(now.date())
print(now.time().strftime("%H:%M:%S"))
sheety_endpoint = "https://api.sheety.co/ccb2a92490be5f6ae86b9f427ccead45/copyOfMyWorkouts/workouts"

sheety_params = {
    "workout": {
        "date": str(now.date()),
        "time": str(now.time().strftime("%H:%M")),
        "exercise": workout,
        "duration": duration,
        "calories": calories
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_params)
# sheety_response.raise_for_status()
data = sheety_response.json()
print(data)