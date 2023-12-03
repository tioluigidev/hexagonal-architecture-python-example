import requests
import json
from application.ports.weather_api_port import WeatherAPIPort
from shared.location_model import LocationModel


class SevenTimerWeatherAPIAdapter(WeatherAPIPort):
    def get_weather_temperature(self, location:LocationModel):
        url = (f'https://www.7timer.info/bin/astro.php?lon={location.longitude}&lat={location.latitude}&ac=0&'
               f'unit=metric&output=json&tzshift=0')
        response = requests.get(url)
        data = json.loads(response.content)
        temperature = float(data['dataseries'][0]['temp2m'])
        return temperature

