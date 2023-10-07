from dotenv import load_dotenv
from icecream import ic
import os
import requests

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = os.environ["SHEET_URL"]
        self.city = ""
        self.iata_code = ""
        self.price = ""
        self.prices = {
            "City": self.city,
            "IATA Code": self.iata_code,
            "Lowest Price": self.price
        }
        self.params = {
            "prices": self.prices
        }
        self.sheet_token = os.environ["SHEET_TOKEN"]
        self.headers = {
            "Authorization": self.sheet_token,
        }


    def update_sheet(self):
        response = requests.post(url=self.sheet_url, json=self.params, headers=self.headers)
        response.raise_for_status()
        return ic(response.json())

    def view_sheet(self):
        response = requests.get(url=self.sheet_url, headers=self.headers)
        response.raise_for_status()
        return ic(response.json())