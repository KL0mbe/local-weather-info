import requests
import os
# city_name = input("please type your city name: ")
# country_code = input("please type your country code: ")
city_name = "ikast"
country_code = "dk"
api_key = os.environ.get("OPEN_WEATHER_API_KEY")
r_location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}")
# &limit={limit}
r_dict = r_location.json()[0]
lat, lon = r_dict["lat"], r_dict["lon"]
r_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
print(r_weather.text)


