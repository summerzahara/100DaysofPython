# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from icecream import ic

data = DataManager()

sheet_data = data.view_sheet()
# ic(sheet_data)

for n in sheet_data:
    if n["iataCode"] == "":
        flight = FlightSearch(n["city"])
        n["iataCode"] = flight.iata_code()

data.data = sheet_data
ic(data.data)
data.update_row()
data.view_sheet()

