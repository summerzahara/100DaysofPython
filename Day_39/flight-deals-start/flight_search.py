from dotenv import load_dotenv
from icecream import ic
import os
import requests
from datetime import datetime as dt, timedelta

load_dotenv()
FLIGHT_URL = os.environ["FLIGHT_URL"]
FLIGHT_API = os.environ["FLIGHT_API_KEY"]
FROM_CITY = "LON"
TODAY = dt.now()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.header = {
            "apikey": FLIGHT_API,
        }

    def iata_code(self):
        params = {
            "term": self.city,
            "location_types": "city",
        }
        response = requests.get(url=f"{FLIGHT_URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        result = response.json()["locations"][0]["code"]
        return result

    def flight_search(self):
        params = {
            "fly_from": FROM_CITY,
            "fly_to": TBD,
            "date_from": (TODAY + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (TODAY + timedelta(days=180)).strftime("%d/%m/%Y"),
            "return_from": (TODAY + timedelta(days=8)).strftime("%d/%m/%Y"),
            "return_to": (TODAY + timedelta(days=29)).strftime("%d/%m/%Y"),
            "curr": "GBP",
        }
        response = requests.get(url=f"{FLIGHT_URL}/v2/search", params=params, headers=self.header)
        response.raise_for_status()


