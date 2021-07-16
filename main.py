from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from NavBar import *
from NewEventPage import *

class Character(Screen):
    pass

class Journal(Screen):
    pass

class Quest(Screen):
    pass

class Shop(Screen):
    pass

sm = ScreenManager()

class Application(App):
    def process_text(self):
        text = self.root.ids.get('input')
        print(text)


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

