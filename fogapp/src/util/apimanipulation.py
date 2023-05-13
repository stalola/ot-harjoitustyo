import json
import os
import sys
from configparser import ConfigParser, NoOptionError
from urllib import parse, error, request


class APIManipulation:
    """Luokka, jonka avulla käsitellään OpenWeather APIn dataa.

    
    """

    def user_input_city(self):
        """Kysyy käyttäjältä kaupungin nimen ja muuttaa sen pienaakkosiksi.

        Returns:
            Merkkijono, joka on käyttäjän antama kaupungin nimi pienaakkosina.
        """
        print("")
        choice = input("Type here the name of the city: ")
        if choice == "":
            sys.exit("You did not type anything -- Exit")
        city = choice.lower()
        return city

    def get_apikey(self):
        """Hakee API-avaimen tiedostosta apikey.ini.

        OpenWeather sääpalvelun APIssa vaadittu API-avain. 
        Voit hankkia oman avaimen osoitteesta 
        https://openweathermap.org/price (valitse Free subscription)

        Returns:
            Merkkijono: API-avain
        """
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


    def access_data(self, city):
        """Metodi, joka tekee API-haun halutun kaupungin säätiedoista 
        OpenWeather-palvelussa.

        Args:
            city (str): Kaupunki, jonka säätietoja halutaan tutkia.

        Returns:
            weatherjson (json): APIsta saatu säädata json-muodossa.

        """
        try:
            url = self.build_api_url(city)
            with request.urlopen(url) as openweather:
                apidata = openweather.read()
                weatherjson = json.loads(apidata)
        except AttributeError as attr_error:
            sys.exit(f"Something went wrong... ({attr_error})")
        except error.HTTPError as http_error:
            if http_error.code == 401:  # 401 - Unauthorized
                sys.exit("Access denied. Check your API key.")
            else:
                sys.exit(f"Something went wrong... (Code {http_error.code})")

        try:
            return weatherjson
        except json.JSONDecodeError:
            sys.exit("Couldn't read the server response.")

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
