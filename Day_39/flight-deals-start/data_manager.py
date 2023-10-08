from dotenv import load_dotenv
from icecream import ic
import os
import requests

load_dotenv()

SHEET_URL = os.environ["SHEET_URL"]
SHEET_TOKEN = os.environ["SHEET_TOKEN"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def view_sheet(self):
        response = requests.get(url=SHEET_URL)
        response.raise_for_status()
        self.data = response.json()["prices"]
        return self.data

    def update_row(self):
        for row in self.data:
            params = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_URL}/{row['id']}",
                json=params
            )
            response.raise_for_status()
            ic(response.json())
