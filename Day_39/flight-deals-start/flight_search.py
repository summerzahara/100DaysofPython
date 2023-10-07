from dotenv import load_dotenv
from icecream import ic
import os
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_url = os.environ["FLIGHT_URL"]
        self.flight_api = os.environ["FLIGHT_API_KEY"]
        self.headers = {
            "apikey": self.flight_api
        }
        self.params = {
            "fly_from": self.flight_origin
            "fly_to": self.flight_dest
        }