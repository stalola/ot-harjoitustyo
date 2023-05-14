from util.apimanipulation import APIManipulation
from util.weatherdata import Weatherdata


class CLI():
    def __init__(self):
        fog = APIManipulation()
        self.instructions()
        print("")
        city_input = fog.user_input_city()
        self.weather = Weatherdata(city_input)

    def instructions(self):
        print("\nFOG APP\n")
        print("- Typing the name of a city will give you the weather")
        print("- Typing nothing will exit")

    def command_line_interface(self):
        city = str(self.weather.city)
        print("")

        print(
            f"{city.upper()} \n")
        print(f"Weather: {self.weather.get_weather('weather_description')}, "
              f"cloudiness: {self.weather.get_weather('clouds')} %\n")
        print(f"Temperature: \t{self.weather.get_temperature('temperature_cels')} C"
              f"\t{self.weather.get_temperature('temperature_fahr')} F ")
        print(f"Feels like: \t{self.weather.get_temperature('feels_like_cels')} C"
              f"\t{self.weather.get_temperature('feels_like_fahr')} F\n")

        print(f"Wind speed: {self.weather.get_wind('wind_speed_met')} met/sec "
              f"{self.weather.get_wind('wind_speed_imp')} mph\n"
              f" and direction: {self.weather.get_wind('wind_direction')}\n")

        print(
            f"Humidity: {self.weather.get_weather('humidity')} % and pressure: "
            f"{self.weather.get_weather('pressure')} hPa \n")

        sunrise = self.weather.get_time("sunrise_local")
        sunset = self.weather.get_time("sunset_local")

        print(f"Sun rises at {sunrise} and sets {sunset}")
        print(f"Last weather update on {self.weather.get_time('date')}")
