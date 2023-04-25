import json
import os
import sys
from configparser import ConfigParser
from urllib import parse, error, request


class FileAction:

    def user_input_fromfile(self):
        # temporary solution until we'll start using API
        print("")
        choice = input("Type here the name of the city: ")
        if choice is None:
            choice = "empty"
        filename = f"{choice.lower()}.json"
        return filename

    def access_data_fromfile(self, filename):
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "..", "data", filename)

        with open(data_file_path, 'r', encoding="utf-8") as weather_file:
            filedata = weather_file.read()

        data = json.loads(filedata)
        return data

    def _get_apikey(self):
        api = ConfigParser()
        api.read("apikey.ini")
        return api["openweather"]["api_key"]

    def build_url(self, user_input):
        weather_api_url = "http://api.openweathermap.org/data/2.5/weather"
        apikey = self._get_apikey()
        city_name = parse.quote_plus(" ".join(user_input))
        url = (
            f"{weather_api_url}?q={city_name}"
            f"&appid={apikey}"
        )
        return url

    def user_input_w_api(self):
        print("")
        choice = input("Type here the name of the city: ")
        if choice is None:
            choice = "empty"
        city = choice.lower()
        return city

    def access_data_w_api(self, url):
        try:
            openweather = request.urlopen(url)
        except error.HTTPError as http_error:
            if http_error.code == 401:  # 401 - Unauthorized
                sys.exit("Access denied. Check your API key.")
            else:
                sys.exit(f"Something went wrong... ({http_error.code})")

        apidata = openweather.read()
        weatherdata = json.loads(apidata)

        try:
            return weatherdata
        except json.JSONDecodeError:
            sys.exit("Couldn't read the server response.")
