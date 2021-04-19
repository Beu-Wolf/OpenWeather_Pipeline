import pandas as pd
from sqlite_connection import DatabaseConnection

        
class ETL_Procedure:
    """Class to execute the ETL procedure in our data
    
    This class executes 3 main steps right now
    1 -> extract the wanted columns from the Dataframe
    2 -> rename the columns to their corresponding name
    3 -> convert Kelvin temperatures to Celsius in relevant columns

    To add more steps simply create the function and add it to the etl_procedure method
    """

    def __init__(self, data_frame: pd.DataFrame):
        """Init attributes, our relevant columns and the Dataframe"""

        self.relevant_columns = DatabaseConnection.columns
        self.data_frame = data_frame


    def extract_wanted_columns(self):
        """Executes step 1 -> extract wanted columns to store"""

        self.data_frame = self.data_frame[self.relevant_columns.keys()]

    def change_cols_to_db_schema(self):
        """Executes step 2 -> change column names to correct names for Database"""

        self.data_frame = self.data_frame.rename(columns=self.relevant_columns)

    def convert_kelvin_celsius(self):
        """Converts relevant columns that have temperature in Kelvin to Celsius"""

        columns = [
        self.relevant_columns['main.temp'], 
        self.relevant_columns['main.temp_min'], 
        self.relevant_columns['main.temp_max'],
        self.relevant_columns['main.feels_like']
        ]

        for column in columns:
            self.data_frame[column] = self.data_frame[column] - 273.15

    def etl_procedure(self):
        """Executes the procedure"""

        self.extract_wanted_columns()
        self.change_cols_to_db_schema()
        self.convert_kelvin_celsius()
        

