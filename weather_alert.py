import requests

parameters = {
    "lon": 15.7766,
    "lat": 50.0407,
    "appid": "9d86c9d55745ef24c7358893e8bd09e8",
    "exclude": "current,minutely,daily",
    "units": "metric"
}


def will_rain():
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    it_will_rain = False
    for hour in range(0, 17):
        condition_code = int(weather_data["hourly"][hour]["weather"][0]["id"])
        if condition_code < 700:
            it_will_rain = True
    return it_will_rain
