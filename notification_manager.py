import requests
API_KEY = "7d63d2cdabd90ac4087738210aeb9ee3-5e7fba0f-b81e10fc"
url = "https://api.mailgun.net/v3/sandboxa9ca99ac25ab49aeaba4636a509ccf1d.mailgun.org/messages"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message_flights, will_rain):
        msg = ""
        if will_rain:
            msg += "It will rain today!\n\n"
        else:
            msg += "It will not rain today\n\n"
        print(len(message_flights))
        if len(message_flights) >= 100:
            msg += message_flights
        else:
            msg += "No cheap tickets for today"
        response = requests.post(url, auth=("api", API_KEY),
                                 data={"from": "Adam <mailgun@sandboxa9ca99ac25ab49aeaba4636a509ccf1d.mailgun.org>",
                                       "to": ["ada.avenger@gmail.com"],
                                       "subject": "Daily notification of informations",
                                       "text": msg})
        response.raise_for_status()
