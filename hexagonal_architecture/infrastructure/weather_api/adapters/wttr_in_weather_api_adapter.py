import requests
import json

from application.ports.weather_api_port import WeatherAPIPort

class WttrInWeatherAPIAdapter(WeatherAPIPort):
    def get_weather_data(self, city):
        response = requests.get(f'https://wttr.in/{city}?format=j1')
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            raise Exception('Error fetching weather data')
        