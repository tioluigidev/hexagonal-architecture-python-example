import sqlite3

from application.ports.database_port import DatabasePort

class SQLite3DatabaseAdapter(DatabasePort):
    def store_weather_temperature(self, temperature):
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY, temperature REAL);')
        cursor.execute(f'INSERT INTO weather (temperature) VALUES ({temperature});')
        conn.commit()
        conn.close()

    def get_latest_weather_temperature(self):
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT temperature FROM weather ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        temperature = result[0]
        conn.close()
        return temperature
        