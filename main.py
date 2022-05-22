import data_manager
import flight_search
import flight_data
import notification_manager
import weather_alert

will_rain = weather_alert.will_rain()

data_sheety = data_manager.DataManager().data
data_flights = flight_search.FlightSearch(data_sheety).flight_search
message_flights = flight_data.FlightData(data_flights).message_flights
notification = notification_manager.NotificationManager(message_flights, will_rain)
