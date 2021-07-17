import json

class EventObject:
    def __init__(self,name,type,day,time_start,time_stop):
        self.name = name
        self.type = type
        self.day = day
        self.time_start = time_start
        self.time_stop = time_stop
        self.id = f"{name}{day}{str(time_start)}"

    def write_to_json(self):
        event_dict = {}
        event_dict[self.id] = {}
        event_dict[self.id]['name'] = self.name
        event_dict[self.id]['type'] = self.type
        event_dict[self.id]['day'] = self.day
        event_dict[self.id]['time_start'] = self.time_start
        event_dict[self.id]['time_stop'] = self.time_stop

        with open('events.json','w') as outfile:
            json.dump(event_dict,outfile)

    def read_from_json(self):
        with open('events.json') as json_file:
            event_dict = json.load(json_file)

        get_id = event_dict[self.id]
        get_name = event_dict[self.id]['name']
        get_type = event_dict[self.id]['type']
        get_day = event_dict[self.id]['day']
        get_time_start = event_dict[self.id]['time_start']
        get_time_stop = event_dict[self.id]['time_stop']
