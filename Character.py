import json

class Character:
    def __init__(self):
        self.hp  = 0
        self.str = 0
        self.int = 0
        self.spt = 0
        self.end = 0

    def write_to_json(self):
        stats = {}
        stats['str'] = self.str
        stats['int'] = self.int
        stats['end'] = self.end
        stats['spt'] = self.spt

        with open('character.json','w') as outfile:
            json.dump(stats,outfile)

    
    def read_from_json(self):
        with open('character.json') as json_file:
            stats = json.load(json_file)

            self.str = stats['str']
            self.int = stats['int']
            self.end = stats['end']
            self.spt = stats['spt']
