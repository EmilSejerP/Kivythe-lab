from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from Player import *
from kivy.uix.floatlayout import FloatLayout
from NavBar import *
from NewEventPage import *

class Character(Screen):
    def __sheet_from_json(self):
        with open('player.json') as json_file:
            stats = json.load(json_file)

        return stats

    def fetch_stat(self,stat):
        stats = self.__sheet_from_json()
        str_val = stats[stat]

        return str(str_val)
    

class Journal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.top_button_share = 1 #size of button

        for key in self.__read_json_entries().keys(): #Fetch all journal entries in the .json
            self.__create_entry2(key)                   #add them as clickable buttons in the journal menu

    def __read_json_entries(self): #for reading journalEntries.json
        try:
            with open('journalEntries.json') as json_file:
                dict = json.load(json_file)
            return dict
        except:
            emptyDict = {}
            return emptyDict

    def __create_entry2(self, name): #create entries in init 
        button_share = \
            Button(pos_hint={"x": 0, "top": self.top_button_share},
                    size_hint_y=None, height=32,text = name)
        button_share.bind(on_release=self.button_load)
        fl = FloatLayout(size_hint_y=None, height=25)
        fl.add_widget(button_share)
        self.ids.box_share.add_widget(fl)

    def create_entry(self):
        if self.create_entries_json() == False: #if we already have the entry in JSON, do not create a new button in the app
            button_share = \
                Button(pos_hint={"x": 0, "top": self.top_button_share},
                       size_hint_y=None, height=32,text = self.ids.title_input.text)
            button_share.bind(on_release=self.button_load)
            fl = FloatLayout(size_hint_y=None, height=25)
            fl.add_widget(button_share)
            self.ids.box_share.add_widget(fl)
        else:
            pass

    def button_load(self, obj):                #make the journal entry text load whenever the corresponding button is pressed in the journal menu.
        print(obj)
        self.ids.input.text = self.__read_json_entries()[obj.text]
        pass

    def create_entries_json(self):              #write entries to .json file
        oldEntries = self.__read_json_entries() #Fetch json objects currently in .json file
        entryName  = self.ids.title_input.text  #Fetch the key name
        text       = self.ids.input.text        #Fetch value
        hasEntry   = False                      #We assume that the map doesnt already contain the key

        if entryName in oldEntries:
            hasEntry = True

        oldEntries[entryName] = text            #insert into the dict

        try:
            with open('journalEntries.json','w') as outfile:
                json.dump(oldEntries,outfile)       #write the dict to .json file
        except:
            print("Something went wrong when writing the journal entry to json. Is journalEntries.json missing?")
            print(oldEntries)

        return hasEntry
    pass

class Quest(Screen):
    pass

class Shop(Screen):
    pass

sm = ScreenManager()

class Application(App):
    player = Player() #move l8r

    def fetch_character_sheet(self): #move l8r
        player.read_from_json() #update char.
        return player

    ##template for property change ##
    #def on_property(self,obj,value): 
    #   print("property change?")

    ##template for event##
    #def on_event(self, obj):
    #    print("Typical event from", obj)

    def on_character_event(self,obj):
        print(obj, " was pressend and the character sheet in app was updated.")
        player.read_from_json()
        player.x


    def build(self):
        nav_bars = NavBar(sm)

        new_event_page = NewEventPage()
        calendar_page = CalendarPage(nav_bars.calender_navbar(new_event_page.create_page()))

        lst = [calendar_page.create_page(),Character(),Journal(),Quest(),Shop()]
        main_box = BoxLayout(orientation="vertical")
        sm.switch_to(lst[0])
        main_box.add_widget(nav_bars.main_navbar(lst))
        main_box.add_widget(sm)
        return main_box

def main():
    Application().run()

if __name__ == '__main__':
    main()

