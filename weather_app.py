import requests
import os
city_name = input("please type your city name: ")
country_code = input("please type your country code: ")
# city_name = "ikast"
# country_code = "dk"
api_key = os.environ.get("OPEN_WEATHER_API_KEY")
r_location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}")
# &limit={limit}
# r_forecast = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric")
r_location_dict = r_location.json()[0]
lat, lon = r_location_dict["lat"], r_location_dict["lon"]
r_curr_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
r_curr_dict = r_curr_weather.json()

print(f"the current weather in {r_curr_dict['name']} is {r_curr_dict['main']['temp']}ºC")


