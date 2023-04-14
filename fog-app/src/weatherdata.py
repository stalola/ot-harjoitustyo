import datetime
from weather import Weather


class Weatherdata:
    def __init__(self, filename):
        self.data = Weather.access_data(self, filename)
        self.city = self.data["name"]
        self.timestamp = self.data["dt"]
        self.date = datetime.datetime.fromtimestamp(self.timestamp)
        self.sunrise_utc = self.data["sys"]["sunrise"]
        self.sunset_utc = self.data["sys"]["sunset"]
        self.temperature_kelv = self.data["main"]["temp"]
        self.feels_like_kelv = self.data["main"]["feels_like"]
        self.temperature_cels = round(self.temperature_kelv-273.15, 1)
        self.feels_like_cels = round(self.feels_like_kelv-273.15, 1)
        self.temperature_fahr = round((self.temperature_kelv-273.15)*9/2+32, 1)
        self.feels_like_fahr = round((self.feels_like_kelv-273.15)*9/2+32, 1)
        self.humidity = self.data["main"]["humidity"]
        self.pressure = self.data["main"]["pressure"]
        self.wind_speed_met = self.data["wind"]["speed"]
        self.wind_speed_imp = round(self.wind_speed_met*2.236936, 2)
        self.wind_deg = self.data["wind"]["deg"]
        self.clouds = self.data["clouds"]["all"]
        self.weather_group = self.data["weather"][0]["main"]
        self.weather_description = self.data["weather"][0]["description"]
        self.weather_icon = self.data["weather"][0]["icon"]
