from abc import ABC, abstractmethod


class DatabasePort(ABC):
    @abstractmethod
    def store_weather_temperature(self, temperature):
        pass

    @abstractmethod
    def get_latest_weather_temperature(self):
        pass
