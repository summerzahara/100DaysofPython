import os
import smtplib

from dotenv import load_dotenv
from icecream import ic
from twilio.rest import Client

load_dotenv()

FROM_CITY = "London-LON"
FROM_EMAIL = os.environ["FROM_EMAIL"]
EMAIL_PASS = os.environ["EMAIL_PASS"]


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

    def send_emails(self, email):
        sender_email = FROM_EMAIL
        password = EMAIL_PASS
        to_email = email

        for message in self.messages:
            # new_message = message.encode("utf-8")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=sender_email, password=password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=to_email,
                    msg=f"Subject:New Deal!\n\n{message}".encode("utf-8"),
                )
