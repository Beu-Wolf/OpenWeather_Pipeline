from dotenv import load_dotenv
import os
import requests
import json



class Data_Fetcher:
    """"Simple class to fecth weather data from OpenWeather API"""

    def __init__(self, base_dir: str):
        """Set the dir to store the helper files"""
        self.base_data_dir = base_dir


    def get_current_weather_of_city(self, city_name: str):
        """API Call, gets our api key from an environment variable and queries the endpoint"""

        load_dotenv()
        payload = {
            'q':city_name,
            'appid': "bad"
        }

        self.json_data = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload).json()

        print(self.json_data)

        if 'cod' in self.json_data:
            if '404' == self.json_data['cod']:
                print(f'Error, city {city_name} not found')
                raise ValueError

    def write_weather_data(self):
        """Stores the JSON received in a helper file. Filename given by city and dt"""

        name = 'current_'+ str(self.json_data['name']) + '_' + str(self.json_data['dt'])
        
        self.filename = os.path.join(os.curdir,self.base_data_dir,r"%s.json" % name)
        
        with open(self.filename, 'w+') as f:
            json.dump(self.json_data, f)



        
