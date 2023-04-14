import datetime
from weather import Weather
from weatherdata import Weatherdata


def main():
    Weather.instructions()
    weather = Weatherdata(Weather.user_input())
    sunrise_ts = datetime.datetime.fromtimestamp(weather.sunrise_utc)
    sunrise_time = sunrise_ts.strftime("%H:%M")
    sunset_ts = datetime.datetime.fromtimestamp(weather.sunset_utc)
    sunset_time = sunset_ts.strftime("%H:%M")

    print("")

    print(f"City: {weather.city} \nTime: {weather.date}")
    print(f"Weather: {weather.weather_group} ({weather.weather_description}), "
          f"cloudiness: {weather.clouds} %\n")
    print(f"Temperature: \t{weather.temperature_cels} C "
          f"\t{weather.temperature_fahr} F \t{weather.temperature_kelv} K")
    print(f"Feels like: \t{weather.feels_like_cels} C "
          f"\t{weather.feels_like_fahr} F \t{weather.feels_like_kelv} K\n")
    print(f"Wind speed: {weather.wind_speed_met} met/sec {weather.wind_speed_imp} "
          f"mph and direction: {weather.wind_deg} degrees")

    print(
        f"Humidity: {weather.humidity} % and pressure: {weather.pressure} hPa \n")
    print(f"Sunrise {sunrise_time} and sunset {sunset_time}")


if __name__ == "__main__":
    main()
