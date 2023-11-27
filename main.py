from application.weather_application_service import WeatherApplicationService
# from infrastructure.database.adapters.sqlite3_database_adapter import SQLite3DatabaseAdapter
from infrastructure.database.adapters.array_database_adapter import ArrayDatabaseAdapter
# from infrastructure.weather_api.adapters.seven_timer_api_adapter import SevenTimerWeatherAPIAdapter
from infrastructure.weather_api.adapters.wttr_in_weather_api_adapter import WttrInWeatherAPIAdapter


if __name__ == '__main__':
    # database = SQLite3DatabaseAdapter()
    database = ArrayDatabaseAdapter()
    # weather_api = SevenTimerWeatherAPIAdapter()
    weather_api = WttrInWeatherAPIAdapter()

    weather_as = WeatherApplicationService(database, weather_api)

    # Fetch and store weather data
    weather_as.fetch_and_store_weather_temperature()

    # Retrieve latest weather data and make a decision
    decision = weather_as.get_decision()
    print(decision)
