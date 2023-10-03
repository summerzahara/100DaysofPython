import requests
from twilio.rest import Client
import os

account_sid = "AC223723d27c55b861eaa06f3f3f08696a"
auth_token = os.environ.get("TWILIO_AUTH")

URL = "https://api.open-meteo.com/v1/forecast"
# LAT = 32.715736
# LONG = -117.161087

LAT = 45.512230
LONG = -122.658722


parameters = {
    "latitude": LAT,
    "longitude": LONG,
    "forecast_days": "2",
    "hourly": {
        "temperature_2m",
        "cloudcover",
    }
}

response = requests.get(URL, params=parameters)

response.raise_for_status()
data = response.json()
# print(data)

hour = data["hourly"]["time"][:12]
cloudy = data["hourly"]["cloudcover"][:12]

print(cloudy)

chance_of_rain = False

for item in cloudy:
    if int(item) > 50:
        chance_of_rain = True

if chance_of_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=os.environ.get("TWILIO_FROM"),
        body="It's going to rain.",
        to=os.environ.get("PHONE")
    )
    print(message.sid, message.status)