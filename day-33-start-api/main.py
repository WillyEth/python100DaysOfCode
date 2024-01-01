import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()

print(data)

longitude = data["iss_position"]["longitude"]

print(longitude)

latitude  = 41.878113
longitude = -87.629799

parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data_2 = response.json()
sunrise = data_2["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_2["results"]["sunset"]
print(data_2)
print(sunrise)
print(sunset)


