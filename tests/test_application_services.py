from application.weather_application_service import WeatherApplicationService
from infrastructure.database.adapters.array_database_adapter import ArrayDatabaseAdapter
from infrastructure.database.adapters.array_database_adapter import table
from infrastructure.weather_api.adapters.seven_timer_api_adapter import SevenTimerWeatherAPIAdapter
from shared.location_model import LocationModel

location = LocationModel('Rio de Janeiro', -22.9035, -43.2069)
database = ArrayDatabaseAdapter()
weather_api = SevenTimerWeatherAPIAdapter()
weather_application_service = WeatherApplicationService(database, weather_api)


def test_weather_as_fetch_and_store_weather_temperature():
    global table
    records = len(table)
    weather_application_service.fetch_and_store_weather_temperature()
    assert len(table) == records + 1
    assert 0 < table[-1] < 100


def test_weather_as_get_decision():
    global table
    table.append(-1)
    assert weather_application_service.get_decision() == {'decision': 'Don''t go outside today'}
    table.append(10)
    assert weather_application_service.get_decision() == {'decision': 'Take a sweater with you'}
    table.append(30)
    assert weather_application_service.get_decision() == {'decision': 'Nice weather to go outside today'}
