from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from Player import *

class Calendar(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_box = BoxLayout(orientation="vertical")
        calendar_page = CalendarPage()
        main_box.add_widget(calendar_page.create_calendar_page())
        self.add_widget(main_box)
    pass

class Character(Screen):
    def change_str_text(self):
        self.ids.str.text = 5
    
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


def switch_to(arg):
    def callback(instance):
        sm.switch_to(arg)
    return callback




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
        main_box = BoxLayout(orientation="vertical")
        box_layout = BoxLayout(size_hint=[1, 0.1])

        calendar_button = Button(text="Calendar")
        calendar_button.bind(on_release=switch_to(Calendar()))
        character_button = Button(text="Character")
        character_button.bind(on_release=switch_to(Character()))
        character_button.bind(on_release=Character.change_str_text)

        journal_button = Button(text="Journal")
        journal_button.bind(on_release=switch_to(Journal()))
        quest_button = Button(text="Quest")
        quest_button.bind(on_release=switch_to(Quest()))
        shop_button = Button(text="Shop")
        shop_button.bind(on_release=switch_to(Shop()))

        box_layout.add_widget(calendar_button)
        box_layout.add_widget(character_button)
        box_layout.add_widget(journal_button)
        box_layout.add_widget(quest_button)
        box_layout.add_widget(shop_button)

        sm.switch_to(Calendar())

        main_box.add_widget(box_layout)
        main_box.add_widget(sm)

        return main_box

def main():
    Application().run()

if __name__ == '__main__':
    main()

