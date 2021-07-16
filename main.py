from kivy.app import App
from CalendarPage import *
from kivy.uix.screenmanager import ScreenManager, Screen

class TestLayout(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_box = BoxLayout(orientation="vertical")

        calendar_page = CalendarPage()

        """
        #create upper menu
        box_layout = BoxLayout(size_hint=[1,0.1])
        box_layout.add_widget(Button(text="Calendar"))
        box_layout.add_widget(Button(text="Character"))
        box_layout.add_widget(Button(text="Journal"))
        box_layout.add_widget(Button(text="Shop"))
        
        main_box.add_widget(box_layout)
        """

        main_box.add_widget(calendar_page.create_calendar_page())

        self.add_widget(main_box)
    pass




class ImANewLayout(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Application(App):

        pass



Application().run()
