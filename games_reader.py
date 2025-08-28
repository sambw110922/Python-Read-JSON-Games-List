
#   13th August 2025.

#   This class reads the JSON and provides the data 
#   to the main file.

#   Import the JSON stuff.
import json 

#   Import single_game
from single_game import *

#   The purpose of this class is to read the JSON file and turn it 
#   into a SingleGame object. 
class GamesReader:

    #   On setup of class
    def __init__(self):

        #   This is the json file path
        self.json_src = "./games_list.json"

        #   This is where I will store the JSON data.
        self.data = ""

        #   Game object array
        self.game_objects = list()

        #   Read the JSON file.
        self.read_json_file()

        #   Turn the data into games
        self.turn_data_into_games()

    #   Actually reads the JSON file
    def read_json_file(self):

        with open(self.json_src, 'r') as file:
            self.data = json.load(file)
        #   end

    #   This turns the data into game objects.
    def turn_data_into_games(self):

        for g in self.data["games"]:

            sg = SingleGame(g["game"], g["platform"])
            self.game_objects.append(sg)
            