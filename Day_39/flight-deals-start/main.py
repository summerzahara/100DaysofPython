# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from icecream import ic

data = DataManager()
#
# sheet_data = data.view_sheet()
# # ic(sheet_data)
#
# for n in sheet_data:
#     if n["iataCode"] == "":
#         flight = FlightSearch(n["city"])
#         n["iataCode"] = flight.iata_code()
#
# data.data = sheet_data
# # ic(data.data)
# data.update_row()
# data.view_sheet()

sheet_data = [
    {
        "city": "Paris",
        "iataCode": "PAR",
        "lowestPrice": 54,
    },
    {
        "city": "Berlin",
        "iataCode": "BER",
        "lowestPrice": 42,
    },
    {
        "city": "Tokyo",
        "iataCode": "TYO",
        "lowestPrice": 485,
    },
    {
        "city": "Sydney",
        "iataCode": "SYD",
        "lowestPrice": 551,
    },
    {
        "city": "Istanbul",
        "iataCode": "IST",
        "lowestPrice": 95,
    },
    {
        "city": "Kuala Lampur",
        "iataCode": "KUL",
        "lowestPrice": 414,
    },
    {
        "city": "New York",
        "iataCode": "NYC",
        "lowestPrice": 240,
    },
    {
        "city": "San Francisco",
        "iataCode": "SFO",
        "lowestPrice": 260,
    },
    {
        "city": "Cape Town",
        "iataCode": "CPT",
        "lowestPrice": 378,
    },
]

search = []
for n in sheet_data:
    trip = FlightSearch(n["city"])
    # ic(n["iataCode"], n["lowestPrice"])
    search = trip.flight_search(iata_code=n["iataCode"], price=n["lowestPrice"])
ic(search)

