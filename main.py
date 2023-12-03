from application.weather_application_service import WeatherApplicationService
# from infrastructure.database.adapters.sqlite3_database_adapter import SQLite3DatabaseAdapter
from infrastructure.database.adapters.array_database_adapter import ArrayDatabaseAdapter
from infrastructure.weather_api.adapters.seven_timer_api_adapter import SevenTimerWeatherAPIAdapter
# from infrastructure.weather_api.adapters.wttr_in_weather_api_adapter import WttrInWeatherAPIAdapter


if __name__ == '__main__':
    # database = SQLite3DatabaseAdapter()
    database = ArrayDatabaseAdapter()
    # weather_api = SevenTimerWeatherAPIAdapter()
    weather_api = SevenTimerWeatherAPIAdapter()

    weather_application_service = WeatherApplicationService(database, weather_api)

    weather_application_service.fetch_and_store_weather_temperature()
    decision = weather_application_service.get_decision()
    print(decision)
