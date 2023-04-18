import json
import os


class FileAction:

    def user_input(self):
        # temporary solution until we'll start using API
        print("")
        choice = input("Type here the name of the city: ")
        if choice is None:
            choice = "empty"
        filename = f"{choice.lower()}.json"
        return filename

    def access_data(self, filename):
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "..", "..", "data", filename)

        with open(data_file_path, 'r', encoding="utf-8") as weather_file:
            filedata = weather_file.read()

        data = json.loads(filedata)
        return data
