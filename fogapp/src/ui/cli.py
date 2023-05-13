import datetime
#import sys

from util.filemanipulation import FileManipulation
from util.weatherdata import Weatherdata


class CLI():
    def __init__(self):
        fog = FileManipulation()
        self.instructions()
        city_input = fog.user_input_w_api()
        self.weather = Weatherdata(city_input)

    def command_line_interface(self):

        print("")

        print(
            f"City: {self.weather.city} \nTime: {self.weather.get_time('date')}")
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
        print("\n\tFOG APP\n")
        print("Typing the name of a city will show you the weather.")
        print("Typing nothing will exit.")

    def get_local_time(self, timestamp):
        timezone_shift = datetime.timezone(
            datetime.timedelta(seconds=self.weather.timezone))
        local_time = datetime.datetime.fromtimestamp(
            timestamp, tz=timezone_shift)
        return local_time.strftime("%H:%M")

    def sunrise(self):
        return self.get_local_time(self.weather.get_time("sunrise_utc"))

    def sunset(self):
        return self.get_local_time(self.weather.get_time("sunset_utc"))
