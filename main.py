from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from Player import *

from NavBar import *
from NewEventPage import *

class Character(Screen):
    pass

class Journal(Screen):
    def print_input_text(self):
        print(self.ids.input.text)
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
        calendar_page = CalendarPage(nav_bars.calender_navbar())
        new_event_page = NewEventPage()
        lst = [calendar_page.create_page(),Character(),Journal(),Quest(),Shop(),new_event_page.create_page()]
        main_box = BoxLayout(orientation="vertical")
        sm.switch_to(lst[0])
        main_box.add_widget(nav_bars.main_navbar(lst))
        main_box.add_widget(sm)
        return main_box

def main():
    Application().run()

if __name__ == '__main__':
    main()

