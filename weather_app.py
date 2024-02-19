import requests
import os
from datetime import datetime
api_key = os.environ.get("OPEN_WEATHER_API_KEY")

while True:
    city_name = input("please type your city name: ")
    country_code = input("please type your country code: ")

    try:
        location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}")
        location.raise_for_status()
        if location.json():
            break
        else:
            print("sorry there is no location with that name or country code\n")
    except requests.RequestException as e:
        print(f"error fetching data : {e}")
        quit()


lat, lon = location.json()[0]["lat"], location.json()[0]["lon"]
curr_weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
forecast_weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric")
curr_dict = curr_weather.json()
forecast_dict = forecast_weather.json()

forecast_temps = {}
for key in forecast_dict["list"]:
    dt = datetime.fromisoformat(key["dt_txt"])
    today = datetime.today().date()
    if dt.date() != today:
        forecast_temps.setdefault(dt.strftime("%A"), []).append(key["main"]["temp"])

for key in forecast_temps:
    forecast_temps[key] = (sum(forecast_temps[key])/len(forecast_temps[key]))

day = 0
forecasts = []
for key in forecast_temps:
    forecasts.append(f"{key} {round(forecast_temps[key], 2)}ºC")
forecasts = "\n".join(forecasts)

print(f"the current weather in {curr_dict['name']} is {curr_dict['main']['temp']}ºC\n"
      f"the weather on the following days will be:\n"
      f"{forecasts}")
