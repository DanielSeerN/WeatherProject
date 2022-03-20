import requests
import datetime
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv('api_key')


def get_current_weather_data(location):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid=' + API_KEY
    response = requests.get(url).json()
    timestamp = response["dt"]
    date = str(datetime.datetime.fromtimestamp(timestamp))
    weather_report = {
        'city': str(response["name"]),
        'date': date,
        'temp': str(response["main"]["temp_min"]) + ' ... ' + str(response["main"]["temp_max"]) + 'C',
        'icon': response["weather"][0]["icon"],
        'humidity': str(response["main"]["humidity"]),
        'pressure': str(response["main"]["pressure"]),
        'wind_speed': str(response["wind"]["speed"]),
    }
    return weather_report


def get_7days_weather_data(coordinates):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={str(coordinates["lat"])}' \
          f'&lon={str(coordinates["lon"])}&exclude=minutely,hourly,alerts&units=metric&appid=' \
          + API_KEY
    response = requests.get(url).json()
    print(response)
    forecast = []
    for i in range(8):
        timestamp = response["daily"][i]["dt"]
        date = str(datetime.datetime.fromtimestamp(timestamp))
        weather_report = {
            'city': str(coordinates["city"]),
            'date': date[:9],
            'temp': str(response["daily"][i]["temp"]["min"]) + ' ... ' + str(response["daily"][i]["temp"]["max"]) + 'C',
            'icon': response["daily"][i]["weather"][0]["icon"],
            'humidity': str(response["daily"][i]["humidity"]),
            'pressure': str(response["daily"][i]["pressure"]),
            'wind_speed': str(response["daily"][i]["wind_speed"]),
            'precipitation_prob': str(response["daily"][i]["pop"]) + '  %'
        }
        forecast.append(weather_report)
    return forecast



