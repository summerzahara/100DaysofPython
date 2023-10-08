from dotenv import load_dotenv
from icecream import ic
import os
import requests
from datetime import datetime as dt, timedelta
from flight_data import FlightData

load_dotenv()
FLIGHT_URL = os.environ["FLIGHT_URL"]
FLIGHT_API = os.environ["FLIGHT_API_KEY"]

TODAY = dt.now()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.header = {
            "apikey": FLIGHT_API,
        }
        self.price_list = []

    def iata_code(self):
        params = {
            "term": self.city,
            "location_types": "city",
        }
        response = requests.get(url=f"{FLIGHT_URL}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        result = response.json()["locations"][0]["code"]
        return result

    def flight_search(self, iata_code, price):
        data = FlightData(iata_code, price)
        params = data.return_attributes()
        response = requests.get(url=f"{FLIGHT_URL}/v2/search", params=params, headers=self.header)
        response.raise_for_status()
        result = response.json()["data"]
        my_list = []
        for item in result:
            ic(f"{item['cityTo']}: £{item['price']}")
            my_list.append([item['cityTo'], item['price']])
            ic(my_list)
        return my_list


