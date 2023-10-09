from icecream import ic
from twilio.rest import Client
from dotenv import load_dotenv
import os, requests

load_dotenv()

FROM_CITY = "London-LON"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, messages):
        self.messages = messages

    def send_notifications(self):
        account_sid = os.environ["TWILIO_SID"]
        auth_token = os.environ["TWILIO_TOKEN"]
        client = Client(account_sid, auth_token)

        for message in self.messages:
            notification = client.messages.create(
                from_=os.environ["TWILIO_PHONE"],
                body=message,
                to=os.environ["USER_PHONE"],
            )
            ic(notification.status)
