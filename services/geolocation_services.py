import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('api_key')


def get_location(search_word):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={search_word}&limit=1&appid=' \
          + API_KEY
    response = requests.get(url).json()
    coordinates = {
        'city': response[0]["name"],
        'lat': response[0]["lat"],
        'lon': response[0]["lon"]
    }
    return coordinates
