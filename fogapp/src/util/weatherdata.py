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

    def get_local_time(self, timestamp):
        """Metodi, jonka avulla voi esittää kellonajan paikallista aikaa.

        Aikaleima muutetaan paikalliseksi ajaksi käyttäen säädatan mukana olevaa
        tietoa sekuntimääräisestä muutoksesta UTC-aikavyöhykkeeseen.

        Args:
            timestamp: Ajanhetki UTC-aikavyöhykkeen aikaleimana

        Returns:
            Kellonaika, jossa on otettu huomioon paikallinen aika.
        """
        timezone_shift = datetime.timezone(
            datetime.timedelta(seconds=self.timezone))
        local_time = datetime.datetime.fromtimestamp(
            timestamp, tz=timezone_shift)
        return local_time.strftime("%H:%M")

    def get_time(self, name):
        """Metodi, joka hakee säädatasta päivämäärän tai auringonnousun tai 
        auringonlaskun ajankohdan.

        Args:
            name (str): toimii arvoilla "date", "sunrise_utc", "sunset_utc",
            "sunrise_local" ja "sunset_local"

        Returns:
            Päivämäärä tai auringonnousun/-laskun aikaleima UTC-aikavyöhykkeellä
            tai kellonaika paikallista aikaa.
        """

        date = datetime.datetime.fromtimestamp(self.timestamp)
        sunrise_utc = self.data["sys"]["sunrise"]
        sunset_utc = self.data["sys"]["sunset"]
        sunrise_local = self.get_local_time(sunrise_utc)
        sunset_local = self.get_local_time(sunset_utc)

        time_values = {"date": date,
                       "sunrise_utc": sunrise_utc,
                       "sunset_utc": sunset_utc,
                       "sunrise_local": sunrise_local,
                       "sunset_local": sunset_local
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
            "wind_deg", "wind_direction"

        Returns:
            tuulennopeus metreinä sekunnissa, maileina tunnissa tai tuulen 
            suunta asteina tai pääilmansuuntana
        """
        wind_speed_met = self.data["wind"]["speed"]
        wind_speed_imp = round(wind_speed_met * 2.236936, 2)
        wind_deg = self.data["wind"]["deg"]
        wind_direction = self.wind_degrees_to_cardinal(wind_deg)

        wind_values = {"wind_speed_met": wind_speed_met,
                       "wind_speed_imp": wind_speed_imp,
                       "wind_deg": wind_deg,
                       "wind_direction": wind_direction
                       }
        return wind_values.get(name, None)

    def wind_degrees_to_cardinal(self, degrees):
        cardinal_directions = {"north": [[348.75, 360], [0, 11.25]],
                               "north-northeast": [11.25, 33.75],
                               "northeast": [33.75, 56.25],
                               "east-northeast": [56.25, 78.75],
                               "east": [78.75, 101.25],
                               "east-southeast": [101.25, 123.75],
                               "southeast": [123.75, 146.25],
                               "south-southeast": [146.25, 168.75],
                               "south": [168.75, 191.25],
                               "south-southwest": [191.25, 213.75],
                               "southwest": [213.75, 236.25],
                               "west-southwest": [236.25, 258.75],
                               "west": [258.75, 281.25],
                               "west-northwest": [281.25, 303.75],
                               "northwest": [303.75, 326.25],
                               "north-northwest": [326.25, 348.75],
                              }

        for cardinal_direction, values in cardinal_directions.items():
            if isinstance(values[0], list):
                for range_list in values:
                    start, end = range_list
                    if start <= degrees <= end:
                        return cardinal_direction
            else:
                start, end = values
                if start <= degrees <= end:
                    return cardinal_direction
        return "unknown"
