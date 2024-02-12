import requests
import os
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

"""need to use datetime module to remove the time from dt_txt
perhaps store date and temp as key value pair in a dict?"""
for key in forecast_dict["list"]:
    print(key["dt_txt"])
    print(key["main"]["temp"])


# print(f"the current weather in {curr_dict['name']} is {curr_dict['main']['temp']}ºC")


