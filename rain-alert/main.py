import requests
import json

API_KEY = "33ffc36b68676b544524f0ca83034ae1"

LATITUDE = 41.836811
LONGITUDE = -87.629799

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

# $https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

conditions = []

for item in data["list"]:
    condition = int(item["weather"][0]["id"])
    conditions.append(condition)


print(conditions)

if max(conditions)<800:
    print("Rain")


# print(json.dumps(data, indent=4))
# weather = data["list"][1]
# print(weather)
# print(data)
