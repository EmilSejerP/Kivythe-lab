import json
from kivy.uix.screenmanager import Screen

class Player:
    def __init__(self):
        self.hp  = 0
        self.str = 0
        self.int = 0
        self.spt = 0
        self.end = 0
        self.inventory = {}

    #writes the character sheet to the json file to save it for l8r
    def write_to_json(self):
        stats = {}
        stats['Strength'] = self.str
        stats['Intelligence'] = self.int
        stats['Endurance'] = self.end
        stats['Spirit'] = self.spt

        with open('player.json','w') as outfile:
            json.dump(stats,outfile)

    #updates the character sheet from the json file
    def read_from_json(self):
        with open('player.json') as json_file:
            stats = json.load(json_file)

        self.str = stats['Strength']
        self.int = stats['Intelligence']
        self.end = stats['Endurance']
        self.spt = stats['Spirit']

    def increase_stat(self,stat,value):
        self.read_from_json()
        if stat == 'Strength':
            self.str += value
        elif stat == 'Intelligence':
            self.int += value
        elif stat == 'Endurance':
            self.end += value
        else:
            self.spt += value
        self.write_to_json()

    