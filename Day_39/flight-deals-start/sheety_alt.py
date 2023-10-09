import os

from dotenv import load_dotenv

load_dotenv()

sheet_data = [
    {
        "city": "Paris",
        "iataCode": "PAR",
        "lowestPrice": 54,
    },
    {
        "city": "Berlin",
        "iataCode": "BER",
        "lowestPrice": 42,
    },
    {
        "city": "Tokyo",
        "iataCode": "TYO",
        "lowestPrice": 485,
    },
    {
        "city": "Sydney",
        "iataCode": "SYD",
        "lowestPrice": 551,
    },
    {
        "city": "Istanbul",
        "iataCode": "IST",
        "lowestPrice": 95,
    },
    {
        "city": "Kuala Lampur",
        "iataCode": "KUL",
        "lowestPrice": 414,
    },
    {
        "city": "New York",
        "iataCode": "NYC",
        "lowestPrice": 240,
    },
    {
        "city": "San Francisco",
        "iataCode": "SFO",
        "lowestPrice": 260,
    },
    {
        "city": "Cape Town",
        "iataCode": "CPT",
        "lowestPrice": 378,
    },
    {
        "city": "Bali",
        "iataCode": "DPS",
        "lowestPrice": 501,
    },
]

user_data = [
    {
        "firstName": "Jane",
        "lastName": "Doe",
        "email": os.environ["TO_EMAIL"],
    },
]