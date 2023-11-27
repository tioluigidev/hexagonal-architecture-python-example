from application.ports.database_port import DatabasePort

table = []

class ArrayDatabaseAdapter(DatabasePort):
    def store_weather_temperature(self, temperature):
        table.append(temperature)

    def get_latest_weather_temperature(self):
        return table[-1]
