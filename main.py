import requests
import json
import os

from twilio.rest import Client
MY_LAT = 38.881622
MY_LON = -77.090981
#twilio data
account_sid = "ACd494b3ca3aaf57b9de845677ef159776"
auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get("API_KEY")
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key

}
#API Data Above, exclude removes certain stats, we just want hourly
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)
#Getting JSON from the data response

#Below I want an if to determine whether we have rain at a particular hour
#need umbrella for any code less than 700

weather_slice = data["hourly"][:12]
print(weather_slice)
condition_codes = []

for hour in weather_slice:
    condition_codes.append(hour["weather"][0]["id"])
print(condition_codes)

will_rain = False
for item in condition_codes:
   if item <= 700:
       will_rain = True

#sends willrain message
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Its going to rain today,bring an umbrella!',
        from_='+19302075053',
        to= os.environ.get("CELL_NUMBER")
    )
    print(message.status)




