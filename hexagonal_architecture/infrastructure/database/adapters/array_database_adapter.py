from application.ports.database_port import DatabasePort

table = []


class ArrayDatabaseAdapter(DatabasePort):
    def store_weather_data(self, temperature, humidity):
        table.append([temperature, humidity])

    def get_latest_weather_data(self):
        return table[-1]