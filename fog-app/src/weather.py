import json
import os

class Weather:
    def instructions():
        #temporary solution until we'll start using API
        print("Choose a city from the list by typing its name: ")
        print("- Helsinki")
        print("- London")
        print("- Paris")
#        print("Typing nothing will exit.")

    def user_input():
        #temporary solution until we'll start using API
            print("")
            choice = input("Type here the name of the city: ")
            if choice == "":
                 return False
            else:
                filename = f"{choice.lower()}.json"
                return filename

    def access_data(filename):
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "data", filename)

        with open(data_file_path, 'r') as weather_file:
            filedata=weather_file.read()

        data = json.loads(filedata)
        return data

