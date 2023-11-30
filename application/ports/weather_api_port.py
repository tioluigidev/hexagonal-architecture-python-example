from abc import ABC, abstractmethod
from shared.model_location import ModelLocation


class WeatherAPIPort(ABC):
    @abstractmethod
    def get_weather_temperature(self, location:ModelLocation):
        pass
