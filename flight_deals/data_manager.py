import requests

SHEETY_API_TOKEN = "kadflkeNCoieeaLLAdafnc"
SHEETY_API_ENDPOINT = "https://api.sheety.co/9bff6130234e71994ddb2b8b752df249/flightDeals/prices"

headers = {
    "Authorization": f"Bearer {SHEETY_API_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        #  Use the Sheety API to GET all the data in that sheet
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)