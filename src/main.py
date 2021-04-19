from sqlite_connection import DatabaseConnection
from data_fetcher import Data_Fetcher
from convert_to_df import convert_json_files_to_df
from etl_procedure import ETL_Procedure
import schedule
import os
import time

###
# Main file, queries OpenWeather every 10 seconds for the current weather in the list of wanted cities
###

cities_file = 'cities-config.txt'
base_data_dir = 'cache'

def job(cities):
    db_conn = DatabaseConnection()

    file_lst = []

    data_fetcher = Data_Fetcher(base_data_dir)

    for city in cities:
        try:
            print(f'Getting information for {city}')
            data_fetcher.get_current_weather_of_city(city)
            data_fetcher.write_weather_data()
            file_lst.append(data_fetcher.filename)
        except ValueError:
            continue

    df = convert_json_files_to_df(file_lst)
    etl = ETL_Procedure(df)
    etl.etl_procedure()
    db_conn.update_db(etl.data_frame)

    print("Database updated....")

    db_conn.close_connection()

    for file in file_lst:
        os.remove(file) # remove helper files

if not os.path.exists(base_data_dir):
    os.makedirs(base_data_dir)

with open(cities_file, 'r') as f:
    cities_lst = f.readlines()
    cities_lst = [x.strip() for x in cities_lst]

# To do it daily just change this line to
# schedule.every().day.at("09:00").do(job, cities=cities_lst)
schedule.every(10).seconds.do(job, cities=cities_lst)

while True:
    schedule.run_pending()
    time.sleep(1)






