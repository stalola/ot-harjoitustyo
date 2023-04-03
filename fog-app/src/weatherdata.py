import datetime
from weather import Weather

class Weatherdata:
    def __init__(self, filename):
        self.data = Weather.access_data(filename)

    def city(self):
        city = self.data["name"]
        return city
    
    def timestamp(self):
        timestamp = self.data["dt"]
        return timestamp
    
    def date(self):
        date = datetime.datetime.fromtimestamp(self.timestamp())
        return date

    def sunrise_utc(self):
        sunrise_utc = self.data["sys"]["sunrise"]
        return sunrise_utc
    
    def sunset_utc(self):
        sunset_utc = self.data["sys"]["sunset"]
        return sunset_utc
    
    def temperature_kelv(self):
        temperature = self.data["main"]["temp"]
        return temperature
    def feels_like_kelv(self):
        feels_like = self.data["main"]["feels_like"]
        return feels_like
    def temperature_cels(self):
        temp_cels = round(self.temperature_kelv()-273.15, 1)
        return temp_cels
    def feels_like_cels(self):
        feels_like_cels = round(self.feels_like_kelv()-273.15, 1)
        return feels_like_cels
    def temperature_fahr(self):
        temp_fahr = round((self.temperature_kelv()-273.15)*9/2+32, 1)
        return temp_fahr
    def feels_like_fahr(self):
        feels_like_fahr = round((self.feels_like_kelv()-273.15)*9/2+32, 1)
        return feels_like_fahr

    def humidity(self):
        humidity = self.data["main"]["humidity"]
        return humidity
    
    def pressure(self):
        pressure = self.data["main"]["pressure"]
        return pressure
    
    def wind_speed_met(self):
        wind_speed_met = self.data["wind"]["speed"]
        return wind_speed_met
    def wind_speed_imp(self):
        wind_speed_imp = round(self.wind_speed_met()*2.236936, 2)
        return wind_speed_imp
    def wind_deg(self):
        wind_deg = self.data["wind"]["deg"]
        return wind_deg
    
    def clouds(self):
        clouds = self.data["clouds"]["all"]
        return clouds
    
    def weather_group(self):
        weather_group = self.data["weather"][0]["main"]
        return weather_group
    
    def weather_description(self):
        weather_description = self.data["weather"][0]["description"]
        return weather_description
    
    def weather_icon(self):
        weather_icon = self.data["weather"][0]["icon"]
        return weather_icon

