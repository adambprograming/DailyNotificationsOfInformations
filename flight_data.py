class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self, data_flights):
        self.approved = []
        for i in range(0, len(data_flights)):
            if data_flights[i] == "No flight found.":
                pass
            else:
                number_of_flights = len(data_flights[i]["route"])
                route = []
                for x in range(0, number_of_flights):
                    route.append(f'{data_flights[i]["route"][x]["cityFrom"]}->{data_flights[i]["route"][x]["cityTo"]}')
                self.approved.append({
                    "cityFrom": data_flights[i]["cityFrom"],
                    "cityTo": data_flights[i]["cityTo"],
                    "price": data_flights[i]["price"],
                    "nightsInDest": data_flights[i]["nightsInDest"],
                    "availableSeats": data_flights[i]["availability"]["seats"],
                    "stopovers": number_of_flights - 2,
                    "route": route,
                    "dateFrom": data_flights[i]["route"][0]["local_departure"].split(".")[0].replace("T", " "),
                    "dateTo": data_flights[i]["route"][number_of_flights - 1]["local_arrival"].split(".")[0].replace(
                        "T", " ")
                })
        length = len(self.approved)
        self.message_flights = "Today´s best prices for selected destinations.\n\n"
        for i in range(0, length):
            self.message_flights += (
                f'Flight from {self.approved[i]["cityFrom"]} to {self.approved[i]["cityTo"]} for '
                f'{self.approved[i]["price"]} CZK. ' 
                f'You will spend {self.approved[i]["nightsInDest"]} nights in destination. '
                f'Only {self.approved[i]["availableSeats"]} seats left! '
                f'Route have {self.approved[i]["stopovers"]} stopover -> {self.approved[i]["route"]}. '
                f'It´s from {self.approved[i]["dateFrom"]} to {self.approved[i]["dateTo"]}\n\n')
