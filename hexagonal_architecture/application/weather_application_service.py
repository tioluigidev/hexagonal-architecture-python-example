from application.ports.database_port import DatabasePort
from application.ports.weather_api_port import WeatherAPIPort

class WeatherApplicationService:
    def __init__(self, 
                 database_port: DatabasePort,
                 weather_api_port: WeatherAPIPort):
        self.database_port = database_port
        self.weather_api_port = weather_api_port

    def fetch_and_store_weather_data(self, city):
        data = self.weather_api_port.get_weather_data(city)
        current_condition = data['current_condition'][0]
        self.database_port.store_weather_data(current_condition['temp_C'], current_condition['humidity'])

    def get_latest_weather_data(self):
        data = self.database_port.get_latest_weather_data()
        return {'temperature': data[0], 'humidity': data[1]}
    