# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from sheety_alt import sheet_data, user_data
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


search = {}
for n in sheet_data:
    trip = FlightSearch(n["city"])
    # ic(n["iataCode"], n["lowestPrice"])
    try:
        search_city, search_price = trip.flight_search(iata_code=n["iataCode"], price=n["lowestPrice"])
        search[search_city] = search_price
    except TypeError:
        pass
# ic(search)

messages = []
for item in sheet_data:
    try:
        if item["lowestPrice"] >= search[item["city"]]:
            message = f"Low price alert! Only £{search[item['city']]} to fly from London to {item['city']}"
            messages.append(message)
    except KeyError:
        pass

notify = NotificationManager(messages)
notify.send_notifications()
for item in user_data:
    notify.send_emails(item["email"])
