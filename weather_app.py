import requests
import os
from datetime import datetime, timedelta
# city_name = input("please type your city name: ")
# country_code = input("please type your country code: ")
city_name = "ikast"
country_code = "dk"
api_key = os.environ.get("OPEN_WEATHER_API_KEY")
location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}")
lat, lon = location.json()[0]["lat"], location.json()[0]["lon"]
curr_weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
forecast_weather = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric")
curr_dict = curr_weather.json()
forecast_dict = forecast_weather.json()

"""functioning temp separator by day; need to attempt it in a for loop to cut down on the if elif length"""
forecast_temps = []
forecast_days = []
for key in forecast_dict["list"]:
    dt = datetime.fromisoformat(key["dt_txt"])
    today = datetime.today().date()
    if dt.date() == today + timedelta(days=1):
        if len(forecast_temps) < 1:
            forecast_temps.append([])
        forecast_temps[0].append(key["main"]["temp"])
        if len(forecast_days) < 1:
            forecast_days.append(dt.strftime("%a"))
    elif dt.date() == today + timedelta(days=2):
        if len(forecast_temps) < 2:
            forecast_temps.append([])
        forecast_temps[1].append(key["main"]["temp"])
        if len(forecast_days) < 2:
            forecast_days.append(dt.strftime("%a"))
    elif dt.date() == today + timedelta(days=3):
        if len(forecast_temps) < 3:
            forecast_temps.append([])
        forecast_temps[2].append(key["main"]["temp"])
        if len(forecast_days) < 3:
            forecast_days.append(dt.strftime("%a"))
    elif dt.date() == today + timedelta(days=4):
        if len(forecast_temps) < 4:
            forecast_temps.append([])
        forecast_temps[3].append(key["main"]["temp"])
        if len(forecast_days) < 4:
            forecast_days.append(dt.strftime("%a"))
    elif dt.date() == today + timedelta(days=5):
        if len(forecast_temps) < 5:
            forecast_temps.append([])
        forecast_temps[4].append(key["main"]["temp"])
        if len(forecast_days) < 5:
            forecast_days.append(dt.strftime("%a"))

forecast_sum = []
for list in forecast_temps:
    forecast_sum.append(sum(list)/len(list))


print(forecast_days)
print(forecast_sum)
print(f"the current weather in {curr_dict['name']} is {curr_dict['main']['temp']}ºC\n"
      f"the average weather tomorrow will be {forecast_sum[0]}ºC")
