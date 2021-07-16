from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class CalendarPage(BoxLayout):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.__setattr__("orientation","vertical")


    def calendar_navbar(self):
        box_layout = BoxLayout(orientation="vertical",size_hint=[1,0.1])
        box_layout.add_widget(Label(text="Im the navbar"))
        self.add_widget(box_layout)

    def create_calendar_page(self):
        self.calendar_navbar()

        grid_layout = GridLayout(cols=8)

        new_box_layout = BoxLayout(orientation="vertical")
        new_box_layout.add_widget(Label(text="Time"))
        for i in range(24):
            new_box_layout.add_widget(Label(text=f"{i + 1}"))
        grid_layout.add_widget(new_box_layout)

        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in week_days:
            new_box_layout = BoxLayout(orientation="vertical")
            new_box_layout.add_widget(Label(text=f"{day}"))
            for i in range(24):
                new_box_layout.add_widget(Label(text=""))
            grid_layout.add_widget(new_box_layout)
        self.add_widget(grid_layout)
        return self

    # def update_calendar(self,start,stop):
