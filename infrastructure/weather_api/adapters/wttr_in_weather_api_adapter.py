import requests
import json
from application.ports.weather_api_port import WeatherAPIPort
from shared.location_model import LocationModel


class WttrInWeatherAPIAdapter(WeatherAPIPort):
    def get_weather_temperature(self, location: LocationModel):
        url = f'https://wttr.in/{location.city}?format=j1'
        response = requests.get(url)
        data = json.loads(response.content)
        temperature = float(data['current_condition'][0]['temp_C'])
        return temperature

