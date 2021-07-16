from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from NewEventPage import *

class CalendarPage(Screen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__setattr__("orientation","vertical")
        self.create_calendar_page()


    def calendar_navbar(self):

        box_layout = BoxLayout(size_hint=[1,0.1])

        new_event_btn = Button(text="+", pos_hint={'right': 1}, size_hint=[0.15, 1],id="new_event_button")

        box_layout.add_widget(Button(text="<", pos_hint={'left':1},size_hint=[0.15,1]))
        box_layout.add_widget(Label(text="What week are we in?", pos_hint={'center': 1}))
        box_layout.add_widget(new_event_btn)
        box_layout.add_widget(Button(text=">", pos_hint={'right':1},size_hint=[0.15,1]))
        return box_layout

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

        box_layout.add_widget(grid_layout)
        self.add_widget(box_layout)
        return self



