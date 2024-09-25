import configparser
import os

from saveinfo import create_file
from userinput import remove_all_spaces

file_name = "configSummarizeArticles.ini"
conf_sections = ["DEFAULT"]
config = configparser.ConfigParser()

def create_confing_file():
    f = open(file_name, "w", encoding="utf-8")
    f.write("[DEFAULT]\n")
    f.write("UseAi = yes\n")
    f.write("TextToSpeech = no\n")
    f.close()

class Confing:
    data = {}

    def set_data_from_confing(self):
        config.read(file_name)
        data = {}
        for section in config:
            data[section] = {}
            for variable in config[section]:
                data[section][variable] = config[section][variable]
        self.data = data

    def __init__(self):
        #check if file exists
        if not os.path.exists(file_name):
            create_confing_file()
        self.set_data_from_confing()

    def use_ai(self):
        result = False

        if remove_all_spaces(self.data['DEFAULT']['useai']).lower() == 'yes':
            print("The ai will summarise the given text!")
            result = True
            return result
        else:
            print("The ai is off, so it will not summarise the given text!")

        return result

