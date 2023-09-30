import datetime as dt
import pandas as pd
import random, smtplib

df = pd.read_csv("birthdays.csv")
bd_list = df.values.tolist()

today = dt.datetime.now()
today_date = (today.month, today.day)
birthday = []

my_email = "s18075970@gmail.com"
my_password = "ygcgcdwfoqfjgrxo"

for item in bd_list:
    if (item[3], item[4]) == today_date:
        birthday.append(item)
        print(f"Today is your birthday! {today_date}")
        birthday_name = birthday[0][0]
        to_email = birthday[0][1]
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            content = letter.readlines()
            print(content)
            message = []
            for n in content:
                new = n.replace("[NAME]", f"{birthday_name}")
                message.append(new)
            output = "".join(message)
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_email, password=my_password)
            connect.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n{output}"
            )
