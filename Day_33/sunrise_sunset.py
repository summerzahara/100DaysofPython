import requests, datetime

MY_LAT = 37.804363
MY_LNG = -122.271111

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])
# print(data)
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

current_time = datetime.datetime.now().hour
print(f"Current Time: {current_time}")


