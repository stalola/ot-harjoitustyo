import datetime
import sys

from util.fileaction import FileAction
from util.weatherdata import Weatherdata


class CLI():
    def __init__(self):
        fog = FileAction()
        self.instructions()
        try:
            self.weather = Weatherdata(fog.user_input_fromfile())
        except:
            sys.exit("You did not type a valid city name -- Exit fogapp")


    def command_line_interface(self):

        print("")

        print(f"City: {self.weather.city} \nTime: {self.weather.get_time('date')}")
        print(f"Weather: {self.weather.get_weather('weather_group')} "
              f"({self.weather.get_weather('weather_description')}), "
              f"cloudiness: {self.weather.get_weather('clouds')} %\n")
        print(f"Temperature: \t{self.weather.get_temperature('temperature_cels')} C"
              f"\t{self.weather.get_temperature('temperature_fahr')} F ")
        print(f"Feels like: \t{self.weather.get_temperature('feels_like_cels')} C"
              f"\t{self.weather.get_temperature('feels_like_fahr')} F \t")
        print(f"Wind speed: {self.weather.get_wind('wind_speed_met')} met/sec "
              f"{self.weather.get_wind('wind_speed_imp')} "
              f"mph and direction: {self.weather.get_wind('wind_deg')} degrees")

        print(
            f"Humidity: {self.weather.get_weather('humidity')} % and pressure: "
            f"{self.weather.get_weather('pressure')} hPa \n")
        print(f"Sunrise {self.sunrise()} and sunset {self.sunset()}")
#        print(f"{self.weather.timezone}")

    def instructions(self):
        print("Choose a city from the list by typing its name: ")
        print("- Helsinki")
        print("- London")
        print("- Paris")
        print("Typing nothing will exit.")

    def sunrise(self):
        sunrise_ts = datetime.datetime.fromtimestamp(
            self.weather.get_time("sunrise_utc"))
        sunrise_hours = sunrise_ts.strftime("%H:%M")
        return sunrise_hours

    def sunset(self):
        sunset_ts = datetime.datetime.fromtimestamp(
            self.weather.get_time("sunset_utc"))
        sunset_hours = sunset_ts.strftime("%H:%M")
        return sunset_hours
