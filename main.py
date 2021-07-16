from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen
from NavBar import *


class Calendar(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_box = BoxLayout(orientation="vertical")
        calendar_page = CalendarPage()
        main_box.add_widget(calendar_page.create_calendar_page())
        self.add_widget(main_box)
    pass

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

    def build(self):
        lst = [Calendar(),Character(),Journal(),Quest(),Shop()]
        nav_bars = NavBar(sm)

        main_box = BoxLayout(orientation="vertical")
        sm.switch_to(Calendar())
        main_box.add_widget(nav_bars.main_navbar(lst))
        main_box.add_widget(sm)

        return main_box

Application().run()
