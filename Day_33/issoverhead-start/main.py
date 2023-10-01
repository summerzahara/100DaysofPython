import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 37.804363
MY_LONG = -122.271111

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

low_lat = iss_latitude - 5
high_lat = iss_latitude + 5
low_lng = iss_longitude - 5
high_lng = iss_longitude + 5


# Your position is within +5 or -5 degrees of the ISS position.
def compare_iss():
    lat_in_range = False
    lng_in_range = False
    if low_lat <= MY_LAT <= high_lat:
        lat_in_range = True
    if low_lng <= MY_LAT <= high_lng:
        lng_in_range = True
    if lat_in_range and lng_in_range:
        return True
    else:
        return False


print(f"ISS Overhead: {compare_iss()}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def check_time():
    is_dark = False
    if sunset >= time_now <= sunrise:
        is_dark = True
    return is_dark


print(f"Is Dark: {check_time()}")

my_email = "s18075970@gmail.com"
my_password = "ygcgcdwfoqfjgrxo"
to_email = "test.user888@yahoo.com"

while True:
    time.sleep(60)
    if compare_iss() and check_time():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:ISS Overhead\n\nLook Up!"
            )
            print("Email sent")
    else:
        print("Not in range")
