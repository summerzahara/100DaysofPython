from dotenv import load_dotenv
import requests, os
import datetime as dt

load_dotenv()

USER_URL = os.environ.get("USER_URL")
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH = "graph1"
TODAY = dt.datetime.now().strftime("%Y%m%d")
YESTERDAY = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "days",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response)

create_pixel_endpoint = f"{graph_endpoint}/{GRAPH}"

pixel_params = {
    "date": TODAY,
    "quantity": "1",
}

# response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{create_pixel_endpoint}/{TODAY}"

update_params = {
    "quantity": "3",
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{create_pixel_endpoint}/{YESTERDAY}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)


