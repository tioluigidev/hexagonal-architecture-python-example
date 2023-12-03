from infrastructure.weather_api.adapters.wttr_in_weather_api_adapter import WttrInWeatherAPIAdapter
from shared.location_model import LocationModel

location = LocationModel('Rio de Janeiro', -22.9035, -43.2069)


def test_wttr_in_weather_api_adapter():
    api = WttrInWeatherAPIAdapter()
    temperature = api.get_weather_temperature(location)
    assert 0 < temperature < 70
