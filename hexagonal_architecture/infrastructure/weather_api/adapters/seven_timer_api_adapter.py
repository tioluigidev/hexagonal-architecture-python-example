import requests
import json

from application.ports.weather_api_port import WeatherAPIPort
from shared.model_location import ModelLocation

class SevenTimerWeatherAPIAdapter(WeatherAPIPort):
    def get_weather_temperature(self, location:ModelLocation):
        url = f'https://www.7timer.info/bin/astro.php?lon={location.longitude}&lat={location.latitude}&ac=0&unit=metric&output=json&tzshift=0'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            temperature = float(data['dataseries'][0]['temp2m'])
            return temperature
        else:
            raise Exception('Error fetching weather data')
