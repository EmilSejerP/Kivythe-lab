from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from TimeScript import *
from datetime import date
class TestLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        time_script = TimeScript()
        grid_layout = GridLayout(cols=7)

        for i in range(time_script.get_day_amount()):
            day = BoxLayout(orientation="vertical")
            day.add_widget(TextInput(text=f"{str(time_script.get_current_time().year)} {str(time_script.get_current_time().month)} {i+1}"))
            day.add_widget(Button(text="Button1"))
            grid_layout.add_widget(day)
        self.add_widget(grid_layout)

    pass



class Application(App):

        pass



Application().run()
