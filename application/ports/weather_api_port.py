from abc import ABC, abstractmethod
from shared.location_model import LocationModel


class WeatherAPIPort(ABC):
    @abstractmethod
    def get_weather_temperature(self, location:LocationModel):
        pass
