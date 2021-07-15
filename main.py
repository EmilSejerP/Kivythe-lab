from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from TimeScript import *

class TestLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        time_script = TimeScript()
        layout = StackLayout()
        elements = BoxLayout(orientation="vertical",size_hint=[1,0.8],pos_hint=["bottom","bottom"])
        layout.add_widget(elements)
        elements.add_widget(Button(text="button1"))
        elements.add_widget(Button(text="button2"))
        self.add_widget(layout)
    pass



class Application(App):

        pass



Application().run()
