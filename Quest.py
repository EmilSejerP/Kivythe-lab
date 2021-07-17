from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class Quest(Screen):
    def __init__(self, **kwargs):
        self.quest_amount = 5;
        pass
    
    def add_quest(self, notice, xpos, ypos):
        self.add_widget(notice)

    def take_quest(self,notice):
        pass

class Notice(BoxLayout):
    def __init__(self, **kwargs):
    