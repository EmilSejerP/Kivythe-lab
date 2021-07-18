import json
class Item:

    def __init__(self,id,name,cost,type,img = None):
        self.id = id
        self.name = name
        self.cost = cost
        self.type = type
        self.img = img if img is not None else ""
        self.write_to_json()

    def write_to_json(self):
        event_dict = self.__read_json_entries()
        event_dict[self.id] = {}
        event_dict[self.id]['name'] = self.name
        event_dict[self.id]['cost'] = self.cost
        event_dict[self.id]['type'] = self.type
        with open('itemDB_placeholder.json', 'w') as outfile:
            json.dump(event_dict, outfile)

    def __read_json_entries(self):
        try:
            with open('itemDB_placeholder.json') as json_file:
                dict = json.load(json_file)
            return dict
        except:
            return {}

