from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()

my_lat = "your latitude"
my_lon = "your longitude"
my_app_key = "your Open weather API key"

parameters = {
    "lat" : my_lat,
    "lon" : my_lon,
    "cnt" : 5,
    "appid": my_app_key,
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params= parameters)
data = response.json()
check_rain = False

for hour_data in data["list"]:
    id = hour_data["weather"][0]["id"]
    if id < 700:
        check_rain = True

if check_rain:
    account_sid = "Your twilio Account sid"
    auth_token = "your auth token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Don't forget umbrella, There are chances of rain today",
        from_="your trial twilio account number",
        to="+92xxxxxxxxxxx",
    )
    print(message.status)



