from abc import ABC, abstractmethod

class WeatherAPIPort(ABC):
    @abstractmethod
    def get_weather_data(self, city):
        pass
