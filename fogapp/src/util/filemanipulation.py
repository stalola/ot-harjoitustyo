import json
import os
import sys
from configparser import ConfigParser, NoOptionError
from urllib import parse, error, request


class FileManipulation:

    def user_input_fromfile(self):
        # temporary solution until we'll start using API
        """FOR TEST USE ONLY
        """
        print("")
        choice = input("Type here the name of the city: ")
        if choice is None:
            choice = "empty"
        filename = f"{choice.lower()}.json"
        return filename

    def access_data_fromfile(self, filename):
        """FOR TEST USE ONLY
        """
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "..", "data", filename)

        with open(data_file_path, 'r', encoding="utf-8") as weather_file:
            filedata = weather_file.read()

        data = json.loads(filedata)
        return data

    def user_input_w_api(self):
        print("")
        choice = input("Type here the name of the city: ")
        if choice is "":
            sys.exit("You did not type anything -- Exit")
        city = choice.lower()
        return city

    def get_apikey(self):
        findkey = ConfigParser()
        findkey.read("src/util/apikey.ini")
        return findkey["openweather"]["api_key"]

    def build_api_url(self, city):
        """Kokoaa URL-osoitteen OpenWeather sää-APIa varten.

        Args: 
            city (str): Kaupungin nimi, joka otetaan käyttäjän syötteestä.

        Returns:
            str: URL, joka hakee argumenttina olevan kaupungin säätiedot
            OpenWeather-palvelusta

        """
        try:
            weather_api_url = "http://api.openweathermap.org/data/2.5/weather"
            apikey = self.get_apikey()
            encoded_city_name = parse.quote_plus(city)
            url = (
                f"{weather_api_url}?q={encoded_city_name}&appid={apikey}"
            )
        except NoOptionError:
            url = None
        return url


    def access_data_w_api(self, city):
        try:
            url = self.build_api_url(city)
            openweather = request.urlopen(url)
        except AttributeError as attr_error:
            sys.exit(f"Something went wrong... ({attr_error})")
        except error.HTTPError as http_error:
            if http_error.code == 401:  # 401 - Unauthorized
                sys.exit("Access denied. Check your API key.")
            else:
                sys.exit(f"Something went wrong... ({http_error.code})")

        apidata = openweather.read()
        weatherjson = json.loads(apidata)

        try:
            return weatherjson
        except json.JSONDecodeError:
            sys.exit("Couldn't read the server response.")