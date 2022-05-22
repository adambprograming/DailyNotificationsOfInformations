import requests
import datetime as dt

API_KEY = "fkgIu2EB5qUOmBmPL5RJbPBm_SmSFEbt"
url = "https://tequila-api.kiwi.com/v2/search"
headers = {
    "apikey": API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # noinspection PyGlobalUndefined
    def __init__(self, data_sheety):
        global data
        self.flight_search = []
        tomorrow = (dt.date.today() - dt.timedelta(days=-1)).strftime("%d/%m/%Y")
        six_months = (dt.date.today() - dt.timedelta(days=-180)).strftime("%d/%m/%Y")
        for i in range(0, len(data_sheety)):
            if data_sheety[i]["dateFrom"] == 0:
                date_from = tomorrow
            else:
                date_from = data_sheety[i]["dateFrom"]
            if data_sheety[i]["dateTo"] == 0:
                date_to = six_months
            else:
                date_to = data_sheety[i]["dateTo"]
            params = {
                "fly_from": "PRG",
                "fly_to": str(data_sheety[i]["iataCode"]),
                "date_from": date_from,
                "dato_to": date_to,
                "nights_in_dst_from": data_sheety[i]["nightMin"],
                "nights_in_dst_to": data_sheety[i]["nightMax"],
                "flight_type": "round",
                "max_stopovers": int(data_sheety[i]["stopovers"]),
                "adults": 1,
                "curr": "CZK",
                "price_from": 0,
                "price_to": int(data_sheety[i]["lowestPrice"]),
                "sort": "price",
                "limit": 1000
            }
            response = requests.get(url=url, headers=headers, params=params)
            # response.raise_for_status()
            try:
                data = response.json()["data"][0]
            except IndexError:
                data = "No flight found."
            finally:
                self.flight_search.append(data)
