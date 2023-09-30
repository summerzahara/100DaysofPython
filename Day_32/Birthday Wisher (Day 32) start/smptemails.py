import smtplib

my_email = "s18075970@gmail.com"
my_password = "ygcgcdwfoqfjgrxo"
to_email = "test.user888@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connect:  # Connect to email address
    connect.starttls()  # Secure connection
    connect.login(user=my_email, password=my_password)
    connect.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Your Mom!\n\nI met your mom last night.")
# connect.close()

