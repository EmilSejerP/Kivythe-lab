from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class Quest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Notice())
        pass
    
    def add_quest(self, notice, xpos, ypos):
        self.add_widget(notice)

    def take_quest(self,notice):
        pass

class Notice(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    