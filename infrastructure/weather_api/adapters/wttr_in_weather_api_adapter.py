import requests
import json
from application.ports.weather_api_port import WeatherAPIPort
from shared.model_location import ModelLocation


class WttrInWeatherAPIAdapter(WeatherAPIPort):
    def get_weather_temperature(self, location:ModelLocation):
        url = f'https://wttr.in/{location.city}?format=j1'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content)
            temperature = float(data['current_condition'][0]['temp_C'])
            return temperature
        else:
            raise Exception('Error fetching weather data')
