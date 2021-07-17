from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from Player import *
from kivy.uix.floatlayout import FloatLayout
from NavBar import *
from NewEventPage import *
from Quest import *
from Shop import *
from Journal import *


class Character(Screen): #should be merged with player.py either by having the player as an object or something else.
    def sheet_from_json(self):
        with open('player.json') as json_file:
            stats = json.load(json_file)

        return stats

    def fetch_stat(self,stat):
        stats = self.sheet_from_json()
        str_val = stats[stat]

        return str(str_val)

class Application(App):
    def init(self, kwargs):
        super().init(kwargs)
        self.sm = ScreenManager()


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

    sm = ScreenManager()

    def build(self):
        nav_bars = NavBar(self.sm)

        new_event_page = NewEventPage()

        lst = [CalendarPage(nav_bars.calender_navbar(new_event_page)),Character(),Journal(),Quest(self.player),Shop()]
        main_box = BoxLayout(orientation="vertical")
        self.sm.switch_to(lst[0])
        main_box.add_widget(nav_bars.main_navbar(lst))
        main_box.add_widget(self.sm)
        return main_box

def main():
    Application().run()


if __name__ == '__main__':
    main()
