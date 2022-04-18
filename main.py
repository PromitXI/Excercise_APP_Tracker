import requests
from datetime import datetime as dt

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

today = dt.now()
date = today.date().strftime("%d/%m/%Y")
time = today.time().strftime("%H:%M:%S")

HEADER = {"Authorization": "Bearer oaskldhioquwue0983reuiowuusakljdkljad0sakjdhyW0E89JSAHD"}

api_id = {
    "x-app-id": "65c2f35d",
    "x-app-key": "203ea5587b616e1636e46594ace0f771"
}

exercise = input("What exercise did you do Today : ")

content = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 92.0,
    "height_cm": 176.0,
    "age": 35
}

sheet_api = "https://api.sheety.co/f79743a891aed1178f9bcb3401343f37/myWorkouts/workouts"

response = requests.post(url=url, headers=api_id, json=content)
data = response.json()
print(data["exercises"])
exercise = (data["exercises"][0]["user_input"]).title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
sheet_input = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
print(sheet_input)

# exercise_data=data[1]
sheet_api = requests.post(url=sheet_api,headers=HEADER, json=sheet_input)
