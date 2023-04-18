from util.weatherdata import Weatherdata

DEGREE_SIGN = "\N{DEGREE SIGN}"

class Fog_ui:
    def __init__(self, filename):
        self.header = "Is it foggy outside?"
        filename = "paris"
        self.weatherdata = Weatherdata(filename)


    def get_city(self):
        return f"{self.weatherdata.city}: "
    
    def get_wind_metric(self):
        return f"{round(self.weatherdata.get_wind('wind_speed_met'))} met/sec"

    def get_wind_imperial(self):
        return f"{round(self.weatherdata.get_wind('wind_speed_imp'))} mph"

    def get_clouds(self):
        return f"{self.weatherdata.get_weather('clouds')} % cloudiness"

    def celsius(self, number):
        return f"{round(number)} {DEGREE_SIGN}C "

    def fahrenheit(self, number):
        return f"{round(number)} {DEGREE_SIGN}F "
# header

#lbl_title.grid(row=0, column=0)

## ask input
#frm_city = tk.Frame(master=self.window, padx=5, pady=5, bg="#9bafc7")
#lbl_input1 = tk.Label(
#    master=frm_city,
#    text="Choose a city: ",
#    fg="#505c68", bg="#9bafc7", padx=5, pady=5
#)
#ent_city1 = tk.Entry(master=frm_city, width=15,
#                     fg="#505c68", bg="#9bafc7")
#lbl_input2 = tk.Label(
#    master=frm_city,
#    text="and another city: ",
#    fg="#505c68", bg="#9bafc7", padx=5, pady=5
#)
#ent_city2 = tk.Entry(master=frm_city, width=15,
#                     fg="#505c68", bg="#9bafc7")
#ent_city2.insert(0, "(optional)")
#
#btn_find = tk.Button(
#    master=frm_city,
#    text="submit",
#    fg="#505c68")
#
#lbl_input1.grid(row=0, column=0)
#ent_city1.grid(row=0, column=1)
#lbl_input2.grid(row=0, column=2)
#ent_city2.grid(row=0, column=3)
#btn_find.grid(row=0, column=4, padx=10)
#
## content
#
#frm_content = tk.Frame(master=self.window, bg="#ffe5de",
#                       borderwidth=1, relief=tk.RAISED)
#lbl_city1 = tk.Label(
#    master=frm_content,
#    text="Portland: ",
#    fg="#505c68",
#    bg="#ffe5de",
#    height=2
#)
#lbl_weather1 = tk.Label(
#    master=frm_content,
#    text="broken clouds",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_temperature1 = tk.Label(
#    master=frm_content,
#    text=f"13 {DEGREE_SIGN}C 55 {DEGREE_SIGN}F",
#    bg="#ffe5de",
#    fg="#505c68",
#    height=2
#)
#lbl_feelslike1 = tk.Label(
#    master=frm_content,
#    text=f"feels like:\n12 {DEGREE_SIGN}C 54 {DEGREE_SIGN}F",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_cloudiness1 = tk.Label(
#    master=frm_content,
#    text="75 % cloudiness",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_wind1 = tk.Label(
#    master=frm_content,
#    text="SSW wind 8 m/s 17 mph",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#
#lbl_City2 = tk.Label(
#    master=frm_content,
#    text="Helsinki: ",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_weather2 = tk.Label(
#    master=frm_content,
#    text="clear sky",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_temperature2 = tk.Label(
#    master=frm_content,
#    text=f"0 {DEGREE_SIGN}C 32 {DEGREE_SIGN}F",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_wind1 = tk.Label(
#    master=frm_content,
#    text="NNE wind 7 m/s 20 mph",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_feelslike2 = tk.Label(
#    master=frm_content,
#    text=f"feels like:\n-4 {DEGREE_SIGN}C 24 {DEGREE_SIGN}F",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#lbl_cloudiness2 = tk.Label(
#    master=frm_content,
#    text="0 % cloudiness",
#    bg="#ffe5de",
#    fg="#505c68"
#)
#
#
## bottom
#
#lbl_bottom1 = tk.Label(
#    master=frm_content,
#    text=" ",
#    bg="#dabeba",
#    width=20
#)
#lbl_bottom2 = tk.Label(
#    master=frm_content,
#    text=" ",
#    bg="#dabeba",
#    width=20
#)
#lbl_bottom3 = tk.Label(
#    master=frm_content,
#    text=" ",
#    bg="#dabeba",
#    width=20
#)
#lbl_bottom4 = tk.Label(
#    master=frm_content,
#    text=" ",
#    bg="#dabeba",
#    width=20
#)
#
#
#lbl_city1.grid(row=0, column=0, sticky="e")
#lbl_weather1.grid(row=0, column=1, sticky="w")
#lbl_temperature1.grid(row=1, column=0, columnspan=2)
#lbl_City2.grid(row=0, column=2, sticky="e")
#lbl_weather2.grid(row=0, column=3, sticky="w")
#lbl_temperature2.grid(row=1, column=2, columnspan=2)
#lbl_feelslike1.grid(row=2, column=0, columnspan=2)
#lbl_feelslike2.grid(row=2, column=2, columnspan=2)
#lbl_cloudiness1.grid(row=3, column=0, columnspan=2)
#lbl_cloudiness2.grid(row=3, column=2, columnspan=2)
#
#lbl_bottom1.grid(row=4, column=0)
#lbl_bottom2.grid(row=4, column=1)
#lbl_bottom3.grid(row=4, column=2)
#lbl_bottom4.grid(row=4, column=3)
#
#
#frm_title.grid(row=0, sticky="nsew")
#frm_city.grid(row=1, sticky="nsew")
#frm_content.grid(row=2, sticky="nsew")
#
#
#self.window.mainloop()
#