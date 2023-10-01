import requests

# Response Codes: 100 - Hold on, not final, 200 - Success, 300 - No permission, 400 - Error, 500 - Server Error

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)  # Response Code: 200
response.raise_for_status()

data = response.json()
pos = data["iss_position"]
lon = float(pos["longitude"])
lat = float(pos["latitude"])
map = (lon, lat)
print(data)
print(pos)
print(map)

