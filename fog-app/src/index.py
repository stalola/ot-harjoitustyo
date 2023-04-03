from weather import Weather
from weatherdata import Weatherdata
import datetime

def main():
    Weather.instructions()
    weather = Weatherdata(Weather.user_input())
    sunrise = datetime.datetime.fromtimestamp(weather.sunrise_utc())
    sr = sunrise.strftime("%H:%M")
    sunset = datetime.datetime.fromtimestamp(weather.sunset_utc())
    ss = sunset.strftime("%H:%M")


    print("")

    print(f"City: {weather.city()} \nTime: {weather.date()}") 
    print(f"Weather: {weather.weather_group()} ({weather.weather_description()}), cloudiness: {weather.clouds()} %\n")
    print(f"Temperature: \t{weather.temperature_cels()} C \t{weather.temperature_fahr()} F \t{weather.temperature_kelv()} K")
    print(f"Feels like: \t{weather.feels_like_cels()} C \t{weather.feels_like_fahr()} F \t{weather.feels_like_kelv()} K\n") 
    print(f"Wind speed: {weather.wind_speed_met()} met/sec {weather.wind_speed_imp()} mph and direction: {weather.wind_deg()} degrees")

    print(f"Humidity: {weather.humidity()} % and pressure: {weather.pressure()} hPa \n")
    print(f"Sunrise {sr} and sunset {ss}")


if __name__ == "__main__":
    main()