# Weather Data pipeling - Python (Mercedes-Benz IO)

This exercise is part of a recruitment process for Mercedes-Benz IO Summer Internships. It consists on creating a data pipelining tool
to gather the current weather data for a number of user specified cities. The data is gathered from the OpenWeather API and added to a database
in order to be used later on.

This application is completely self-contained meaning it can be easily be run in containers.

## How to run

### Before

- Make sure you have a valid API key for OpenWeathen.
- Add you api key to the `.env` file present with property name `API_KEY`, if you want to run locally
- Write the cities you want to gather data about in file `cities-config.txt`. Make sure to use capitalization and correctly write the city name in English

### Run

#### Locally

- To run locally, make sure to have your api key in the `.env` file as stated above
- run `python3 main.py` in your terminal

#### Docker

- You use Docker, you don't need the `.env` file
- There is a `Dockerfile` provided that will execute the steps and download the required packages
- Run `docker build . -t <dockerId>/<name>`, for example `docker build . -t daniel/weather` to build the image
- Run `docker run --env API_KEY=<apiKey> -it <dockerId>/<name>`, for example `docker run --env API_KEY="123" -it daniel/weather`

## NOTES

Somethings could be improved like being able to easily add more columns to our table or create a more complex schema.
Since this will be in a public repository, I will not put my API key here so the project does not work until you had your own