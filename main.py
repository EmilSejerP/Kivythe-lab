from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from TimeScript import *
from CalendarPage import *

class TestLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        calendar_page = CalendarPage()
        #create upper menu
        box_layout = BoxLayout(size_hint=[1,0.1])
        box_layout.add_widget(Button(text="Calendar"))
        box_layout.add_widget(Button(text="Character"))
        box_layout.add_widget(Button(text="Journal"))
        box_layout.add_widget(Button(text="Shop"))
        self.__setattr__("orientation", "vertical")
        self.add_widget(box_layout)
        self.add_widget(calendar_page.create_calendar_page())
        #create month layout
        """grid_layout = GridLayout(cols=7,size_hint=[1,0.9])
        for i in range(time_script.get_day_amount()):
            day = BoxLayout(orientation="vertical",
                            size_hint=[0.5,None])
            if time_script.get_current_time().day == i+1:
                day.add_widget(Label(text=f"Currenday!",
                                     size_hint = [None,0.2]))
                day.add_widget(Button(text="Button1"))
            else:
                day.add_widget(Label(text=f"{str(time_script.get_current_time().year)} "
                                          f"{str(time_script.get_current_time().month)} "
                                          f"{i+1}",
                                     size_hint = [None,0.2]))
            #day.add_widget(Button(text="Button1"))
            grid_layout.add_widget(day)
        self.__setattr__("orientation","vertical")
        self.add_widget(box_layout)
        self.add_widget(grid_layout)"""


        pass



class Application(App):

        pass



Application().run()
