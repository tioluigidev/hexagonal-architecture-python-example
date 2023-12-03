from infrastructure.database.adapters.array_database_adapter import ArrayDatabaseAdapter

database = ArrayDatabaseAdapter()


def test_array_database_adapter():
    database = ArrayDatabaseAdapter()
    database.store_weather_temperature(-10000)
    temperature = database.get_latest_weather_temperature()
    assert temperature == -10000
