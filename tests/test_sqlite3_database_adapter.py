from infrastructure.database.adapters.sqlite3_database_adapter import SQLite3DatabaseAdapter


def test_sqlite3_database_adapter():
    database = SQLite3DatabaseAdapter()
    database.store_weather_temperature(-10001)
    temperature = database.get_latest_weather_temperature()
    assert temperature == -10001
