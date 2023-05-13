import datetime
from util.filemanipulation import FileManipulation


class Weatherdata:
    def __init__(self, city_input):
        fog = FileManipulation()
        self.data = fog.access_data_w_api(city_input)
        self.city = self.data["name"]
        self.timestamp = self.data["dt"]
        self.timezone = self.data["timezone"]

    def get_time(self, name):
        date = datetime.datetime.fromtimestamp(self.timestamp)
        sunrise_utc = self.data["sys"]["sunrise"]
        sunset_utc = self.data["sys"]["sunset"]
        time_values = {"date": date,
            "sunrise_utc": sunrise_utc,
            "sunset_utc": sunset_utc
        }
        return time_values.get(name, None)
    
    def get_temperature(self, name):
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
        humidity = self.data["main"]["humidity"]
        pressure = self.data["main"]["pressure"]
        clouds = self.data["clouds"]["all"]
        weather_group = self.data["weather"][0]["main"]
        weather_description = self.data["weather"][0]["description"]
        weather_icon = self.data["weather"][0]["icon"]
        weather_values = {
            "humidity": humidity,
            "pressure": pressure,
            "clouds": clouds,
            "weather_group": weather_group,
            "weather_description": weather_description,
            "weather_icon": weather_icon
            }
        return weather_values.get(name, None)

    def get_wind(self, name):
        wind_speed_met = self.data["wind"]["speed"]
        wind_speed_imp = round(wind_speed_met*2.236936, 2)
        wind_deg = self.data["wind"]["deg"]
        wind_values = {
            "wind_speed_met": wind_speed_met,
            "wind_speed_imp": wind_speed_imp,
            "wind_deg": wind_deg
        }
        return wind_values.get(name, None)
