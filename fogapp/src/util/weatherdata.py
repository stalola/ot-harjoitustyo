import datetime
from util.apimanipulation import APIManipulation


class Weatherdata:
    """Luokka, joka käsittelee OpenWeather -palvelun API-dataa.
    """

    def __init__(self, city_input):
        """Luokan konstruktori, joka luo APIManipulation -luokan avulla json-muotoisen säädatan.

        Args:
            city_input (str): Kaupungin nimi, jonka säädataa halutaan käsitellä.
        """
        fog = APIManipulation()
        self.data = fog.access_data(city_input)
        self.city = self.data["name"]
        self.timestamp = self.data["dt"]
        self.timezone = self.data["timezone"]

    def get_time(self, name):
        """Metodi, joka hakee säädatasta päivämäärän tai auringonnousun tai 
        auringonlaskun ajankohdan.

        Args:
            name (str): toimii arvoilla "date", "sunrise_utc" ja "sunset_utc"

        Returns:
            Päivämäärä tai auringonnousun/-laskun aikaleima UTC-aikavyöhykkeellä.
        """

        date = datetime.datetime.fromtimestamp(self.timestamp)
        sunrise_utc = self.data["sys"]["sunrise"]
        sunset_utc = self.data["sys"]["sunset"]

        time_values = {"date": date,
                       "sunrise_utc": sunrise_utc,
                       "sunset_utc": sunset_utc
                       }
        return time_values.get(name, None)

    def get_temperature(self, name):
        """Metodi, joka hakee säädatasta lämpötilan.

        Args:
            name (str): toimii arvoilla "temperature_cels", "temperature_fahr", 
            "feels_like_cels", ja "feels_like_fahr"

        Returns:
            Lämpötila tai tuntuu-kuin-lämpötila celsius- tai 
            fahrenheitasteissa
        """
        temperature_kelv = self.data["main"]["temp"]
        feels_like_kelv = self.data["main"]["feels_like"]
        temperature_cels = round(temperature_kelv - 273.15, 1)
        feels_like_cels = round(feels_like_kelv - 273.15, 1)
        temperature_fahr = round((temperature_kelv - 273.15) * 9 / 5 + 32, 1)
        feels_like_fahr = round((feels_like_kelv - 273.15) * 9 / 5 + 32, 1)

        temperature_values = {"temperature_cels": temperature_cels,
                              "temperature_fahr": temperature_fahr,
                              "feels_like_cels": feels_like_cels,
                              "feels_like_fahr": feels_like_fahr}
        return temperature_values.get(name, None)

    def get_weather(self, name):
        """Metodi, joka hakee säädatasta säätietoja.

        Args:
            name (str): toimii arvoilla "humidity", "pressure", "clouds", 
            "weather_group", "weather_description", "weather_icon"

        Returns:
            ilmankosteus, ilmanpaine, pilvisyys, sää, sään sanallinen kuvaus 
            tai sää-ikonin tiedostonimi
        """
        humidity = self.data["main"]["humidity"]
        pressure = self.data["main"]["pressure"]
        clouds = self.data["clouds"]["all"]
        weather_group = self.data["weather"][0]["main"]
        weather_description = self.data["weather"][0]["description"]
        weather_icon = self.data["weather"][0]["icon"]

        weather_values = {"humidity": humidity,
                          "pressure": pressure,
                          "clouds": clouds,
                          "weather_group": weather_group,
                          "weather_description": weather_description,
                          "weather_icon": weather_icon
                          }
        return weather_values.get(name, None)

    def get_wind(self, name):
        """Metodi, joka hakee säädatasta tuulta koskevat tiedot.

        Args:
            name (str): toimii arvoilla "wind_speed_met", "wind_speed_imp", 
            "wind_deg"

        Returns:
            tuulennopeus metreinä sekunnissa, maileina tunnissa tai tuulen 
            suunta asteina
        """
        wind_speed_met = self.data["wind"]["speed"]
        wind_speed_imp = round(wind_speed_met * 2.236936, 2)
        wind_deg = self.data["wind"]["deg"]

        wind_values = {"wind_speed_met": wind_speed_met,
                       "wind_speed_imp": wind_speed_imp,
                       "wind_deg": wind_deg
                       }
        return wind_values.get(name, None)
