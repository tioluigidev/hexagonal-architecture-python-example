from abc import ABC, abstractmethod

class DatabasePort(ABC):
    @abstractmethod
    def store_weather_data(self, temperature, humidity):
        pass

    @abstractmethod
    def get_latest_weather_data(self):
        pass
    