# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import get_destination_code, check_flights
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "BLR"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:
    flight = check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight:
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only Rs.{flight.price} to fly "
                        f"from {flight.origin_city}-{flight.origin_airport} "
                        f"to {flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} "
                        f"to {flight.return_date}."
            )