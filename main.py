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
    pass

class Journal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.top_button_share = 1
        self.top_label_share = 2.3

    def print_input_text(self):
        print(self.ids.input.text)

    def save_to_json(self):
        pass

    def create_entry(self):
        self.top_button_share -= 0
        self.top_label_share -= 0
        button_share = \
            Button(pos_hint={"x": 0, "top": self.top_button_share},
                   size_hint_y=None, height=32)
        label_share = \
            Label(text=str(self.ids.title_input.text), pos_hint={"x": 0, "top": self.top_label_share},
                  size_hint_y=None)
        button_share.bind(on_release=self.button_load)
        fl = FloatLayout(size_hint_y=None, height=25)
        fl.add_widget(button_share)
        fl.add_widget(label_share)
        self.ids.box_share.add_widget(fl)

    def button_load(self, obj):
        self.ids.input.text = name
        pass
    def create_entries_json(self):
        pass
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

