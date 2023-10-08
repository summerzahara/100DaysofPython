from datetime import datetime as dt, timedelta

TODAY = dt.now()
CURRENCY = "GBP"
FROM_CITY = "LON"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, iata_code, price):
        self.fly_to = iata_code
        self.date_from = (TODAY + timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (TODAY + timedelta(days=180)).strftime("%d/%m/%Y")
        # self.return_from = (TODAY + timedelta(days=8)).strftime("%d/%m/%Y")
        # self.return_to = (TODAY + timedelta(days=29)).strftime("%d/%m/%Y")
        self.currency = CURRENCY
        self.price_to = price
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.one_for_city = 1
        self.max_stopovers = 0
        self.ret_from_diff_city = False
        self.ret_to_diff_city = False

    def return_attributes(self):
        params = {
            "fly_from": FROM_CITY,
            "fly_to": self.fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "one_for_city": self.one_for_city,
            "max_stopovers": self.max_stopovers,
            "curr": self.currency,
            "ret_from_diff_city": self.ret_from_diff_city,
            "ret_to_diff_city": self.ret_to_diff_city,
        }
        return params
