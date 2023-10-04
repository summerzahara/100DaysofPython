# Object Oriented Programming
```python
class Car:
    def __init__(self):
        self.make = "Tesla"
        self.model = "Model S"
        self.year = 2022
        self.color = "gray"
```

# Tkinter GUIs
```python
from tkinter import *

window = Tk()
window.title("App Title")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20, bg="white")

window.mainloop()
```

# Typing
```python
age: int
name: string
height: float
is_human: bool

def my_func(data: int) -> bool:
    plus_5 = 5 + data
    if plus_5 > 10:
        return True
    else:
        return False
```

# Environment Variables
```zsh
export API_KEY=834389049038490
env
```

```python
import os

api_key = os.environ.get("API_KEY")
```



# APIs
```python
import requests

parameters = {
    "param": MY_PARAM,
    "another_param": YOUR_PARAM,
}

response = requests.get("http://api-url.json", params=parameters)
response.raise_for_status()
data = response.json()
```

# Dates and Times

```python
from datetime import datetime as dt

time = dt.now()
year = dt.year
month = dt.month
day = dt.day
day_of_week = dt.weekday() # response is index
hour = dt.hour
```

# Emails
```python
import smtplib

sender_email = "email@email.com"
password = "secretpassword"
to_email = "youremail@email.com" 

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #secure connection
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=to_email,
        msg="Subject:EmailSubject\n\nYour email body."
    )
```

# Files
```python
with open("data.txt", "a") as file:
    file.write("Write to the file")
```

## JSON
```python
import json

with open ("data.json", "r") as file:
    data = json.load(file) # read file
    data.update(new_file) # append file

with open("data.json", "w") as file:
    data = json.dump(new_file, file, indent=4) # create a file and write

```

# Unescape HTML encoding
```python
import html

copyright = "&copy; 2023 Summer. All rights reserved."
html.unescape(copyright)
```