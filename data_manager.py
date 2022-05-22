import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        response = requests.get(url="https://api.sheety.co/fe7f8da88766633c24e1b0176fbcabc3/flights/prices")
        response.raise_for_status()
        self.data = response.json()["prices"]
