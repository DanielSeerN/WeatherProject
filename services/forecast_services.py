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
        'temp': str(response["main"]["temp"]) + 'C',
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
            'date': date[:10],
            'temp': str(response["daily"][i]["temp"]["min"]) + ' ... ' + str(response["daily"][i]["temp"]["max"]) + 'C',
            'icon': response["daily"][i]["weather"][0]["icon"],
            'humidity': str(response["daily"][i]["humidity"]),
            'pressure': str(response["daily"][i]["pressure"]),
            'wind_speed': str(response["daily"][i]["wind_speed"]),
            'precipitation_prob': str(response["daily"][i]["pop"]) + '  %',
            'morn_temp': str(response["daily"][i]["temp"]["morn"]) + 'C',
            'day_temp': str(response["daily"][i]["temp"]["day"]) + 'C',
            'eve_temp': str(response["daily"][i]["temp"]["eve"]) + 'C',
            'night_temp': str(response["daily"][i]["temp"]["night"]) + 'C',
        }
        forecast.append(weather_report)
    return forecast



