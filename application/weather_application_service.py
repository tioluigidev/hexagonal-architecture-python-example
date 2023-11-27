from application.ports.database_port import DatabasePort
from application.ports.weather_api_port import WeatherAPIPort
from shared.model_location import ModelLocation
from domain.location_domain_service import LocationDomainService
from domain.decision_domain_service import DecisionDomainService


class WeatherApplicationService:
    database_port: DatabasePort
    weather_api_port: WeatherAPIPort
    location: ModelLocation

    def __init__(self, 
                 database_port: DatabasePort,
                 weather_api_port: WeatherAPIPort):
        self.database_port = database_port
        self.weather_api_port = weather_api_port
        self.location = LocationDomainService.get_location()

    def fetch_and_store_weather_temperature(self):
        temperature = self.weather_api_port.get_weather_temperature(self.location)
        self.database_port.store_weather_temperature(temperature)

    def get_decision(self):
        temperature = self.database_port.get_latest_weather_temperature()
        decision = DecisionDomainService.get_decision(temperature)
        return {'decision': decision}
