import sqlite3
import pandas as pd


class DatabaseConnection:
    """ Class to represent the connection to the database

    This class will create a connection to a sqlite database and 
    update the table according to a pandas Dataframe
    """

    dabatabase_name = "WeatherDB.db"

    # mapping from the names of the Json received in the OpenWeather API to the column names of the table
    columns =  {
        'name': 'name', 
        'dt': 'dt',
        'visibility': 'visibility', 
        'main.temp': 'temp', 
        'main.feels_like': 'feels_like', 
        'main.temp_min': 'temp_min', 
        'main.temp_max': 'temp_max', 
        'main.pressure': 'pressure', 
        'main.humidity': 'humidity', 
        'wind.speed': 'wind_speed', 
        'wind.deg': 'wind_deg'
    }

    # Initial statetement to create the table
    _create_table_stm = """CREATE TABLE IF NOT EXISTS Weather (
        name text,
        dt integer,
        visibility integer NOT NULL,
        temp real NOT NULL,
        feels_like real NOT NULL,
        temp_min real NOT NULL,
        temp_max real NOT NULL,
        pressure integer NOT NULL,
        humidity integer NOT NULL,
        wind_speed real NOT NULL,
        wind_deg integer NOT NULL,
        PRIMARY KEY (name, dt)
    );"""

    def __init__(self):
        """Creates connection to the database and creates the table"""

        self.connection = sqlite3.connect(self.dabatabase_name, uri=True)
        self.connection.cursor()
        self.connection.execute(self._create_table_stm)
        self.connection.commit()


    def close_connection(self):
        """Closes the connection to the database"""
        self.connection.close()

    def update_db(self, data_frame: pd.DataFrame):
        """For each row of the received Dataframe, adds it if not already present"""

        cols = "`,`".join([str(i) for i in data_frame.columns.tolist()])
        for _, row in data_frame.iterrows():
            sql = "INSERT OR IGNORE INTO Weather (`" + cols + "`) VALUES (" + "?,"*(len(row)-1) + "?)"
            self.connection.execute(sql, tuple(row))
            self.connection.commit()
