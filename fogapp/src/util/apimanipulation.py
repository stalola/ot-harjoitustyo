import json
import sys
from configparser import ConfigParser, NoOptionError
from urllib import parse, error, request


class APIManipulation:
    """Luokka, jonka avulla käsitellään OpenWeather APIn dataa.

    
    """

    def user_input_city(self):
        """Metodi, joka kysyy käyttäjältä kaupungin nimen ja muuttaa sen 
        pienaakkosiksi.

        Returns:
            Merkkijono, joka on käyttäjän antama kaupungin nimi pienaakkosina.
        """
        choice = input("Type here the name of the city: ")
        if choice == "":
            sys.exit("You did not type anything -- Exit")
        city = choice.lower()
        return city

    def new_apikey(self):
        """Metodi, joka lisää käyttäjän API-avaimen tiedostoon apikey.ini.

        Jos tiedostoa apikey.ini ei ole, metodi luo uuden tiedoston.
        Voit hankkia oman ilmaisen OpenWeather-palvelun API-avaimen osoitteesta 
        https://home.openweathermap.org/users/sign_up
        """
        newapi = input("Type here the new api key (typing nothing will exit "
                       "without changes): ")
        if newapi == "":
            sys.exit("Exiting.. API key was not changed.")
        with open("src/util/apikey.ini", "w", encoding="utf-8") as keyfile:
            keyfile.write(f"[openweather]\napi_key={newapi}")
        print(f"Avain {newapi} lisätty tiedostoon apikey.ini")

    def get_apikey(self):
        """Hakee API-avaimen tiedostosta apikey.ini.

        OpenWeather sääpalvelun APIssa vaadittu API-avain. 
        Voit hankkia oman ilmaisen avaimen osoitteesta 
        https://home.openweathermap.org/users/sign_up

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
