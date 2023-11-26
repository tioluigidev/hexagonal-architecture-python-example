import sqlite3

from application.ports.database_port import DatabasePort

class SQLite3DatabaseAdapter(DatabasePort):
    def store_weather_data(self, temperature, humidity):
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY, temperature REAL, humidity REAL)')
        cursor.execute('INSERT INTO weather (temperature, humidity) VALUES (?, ?)', (temperature, humidity))
        conn.commit()
        conn.close()

    def get_latest_weather_data(self):
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT temperature, humidity FROM weather ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        conn.close()
        return result        
        