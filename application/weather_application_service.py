from application.ports.database_port import DatabasePort
from application.ports.weather_api_port import WeatherAPIPort
from shared.location_model import LocationModel
from domain.location_domain_service import LocationDomainService
from domain.decision_domain_service import DecisionDomainService


class WeatherApplicationService:
    def __init__(self, 
                 database: DatabasePort,
                 weather_api: WeatherAPIPort):
        self.database = database
        self.weather_api = weather_api
        self.location = LocationDomainService.get_location()

    def fetch_and_store_weather_temperature(self):
        temperature = self.weather_api.get_weather_temperature(self.location)
        self.database.store_weather_temperature(temperature)

    def get_decision(self):
        temperature = self.database.get_latest_weather_temperature()
        decision = DecisionDomainService.get_decision(temperature)
        return {'decision': decision}
