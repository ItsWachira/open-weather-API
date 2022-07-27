import requests

from twilio.rest import Client

account_sid = "Account ssd"
auth_token = "Your twillio Auth token"

API_KEY = "Your OWM API KEY"
OWM_endpoint = "http://api.openweathermap.org/data/2.5/weather"

weather_parameter = {
    "q": "Nairobi, Kenya",
    "APPID": API_KEY
}
response = requests.get(OWM_endpoint, params=weather_parameter)
response.raise_for_status()

all_api_data = response.json()
weather_data = all_api_data["weather"][0]["id"]
print(weather_data)

will_rain = False
if weather_data > 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey, Carry an umbrella  its about to rain.",
        from_='+15017122661',
        to='+254113877811'
    )

    print(message.status)
