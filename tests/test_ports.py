from application.ports.database_port import DatabasePort
from application.ports.weather_api_port import WeatherAPIPort
from shared.location_model import LocationModel
from dataclasses import dataclass
from abc import ABCMeta


def test_database_port():
    DatabasePort.__abstractmethods__ = set()

    @dataclass
    class Database(DatabasePort):
        pass

    database = Database()
    store_weather_temperature = database.store_weather_temperature(0)
    get_latest_weather_temperature = database.get_latest_weather_temperature()
    assert isinstance(Database, ABCMeta)
    assert store_weather_temperature is None
    assert get_latest_weather_temperature is None


def test_weather_api_port():
    WeatherAPIPort.__abstractmethods__ = set()

    @dataclass
    class WeatherApi(WeatherAPIPort):
        pass

    weather_api = WeatherApi()
    get_weather_temperature = weather_api.get_weather_temperature(LocationModel('Test', 0, 0))
    assert isinstance(WeatherAPIPort, ABCMeta)
    assert get_weather_temperature is None
