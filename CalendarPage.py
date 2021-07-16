from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from NewEventPage import *

class CalendarPage(Screen):

    def __init__(self,navbar,**kwargs):
        super().__init__(**kwargs)
        self.__setattr__("orientation","vertical")
        self.navbar = navbar

    def create_calendar_page(self):
        box_layout = BoxLayout(orientation="vertical")

        grid_layout = GridLayout(cols=8)

        new_box_layout = BoxLayout(orientation="vertical")
        new_box_layout.add_widget(Label(text="Time"))
        for i in range(24):
            new_box_layout.add_widget(Label(text=f"{i + 1}:00"))
        grid_layout.add_widget(new_box_layout)

        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in week_days:
            new_box_layout = BoxLayout(orientation="vertical")
            new_box_layout.add_widget(Label(text=f"{day}"))
            for i in range(24):
                new_box_layout.add_widget(Label(text=""))
            grid_layout.add_widget(new_box_layout)

        box_layout.add_widget(self.navbar)
        box_layout.add_widget(grid_layout)
        self.add_widget(box_layout)
        return self



