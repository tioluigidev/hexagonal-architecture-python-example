from infrastructure.weather_api.adapters.seven_timer_api_adapter import SevenTimerWeatherAPIAdapter
from shared.location_model import LocationModel

location = LocationModel('Rio de Janeiro', -22.9035, -43.2069)


def test_seven_timer_weather_api_adapter():
    api = SevenTimerWeatherAPIAdapter()
    temperature = api.get_weather_temperature(location)
    assert 0 < temperature < 70
