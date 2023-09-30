import smtplib
import datetime as dt
import pandas as pd
from random import choice
import smtplib

my_email = "s18075970@gmail.com"
my_password = "ygcgcdwfoqfjgrxo"
to_email = "test.user888@yahoo.com"

df = pd.read_csv("quotes.txt")
quote_list = df.values.tolist()
quote = choice(quote_list)[0]
print(quote)

today = dt.datetime.now()
if today.weekday() == 4:
    print("success")
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=my_email, password=my_password)
        connect.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Your Friday Quote!\n\n{quote}"
        )


