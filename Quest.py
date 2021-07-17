from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Quest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.notice = Notice()

        self.notice.text = "place 2 workout hours in a week." 

        self.notice.bind(on_release=self.on_accepted_quest)




        self.ids.available_quests.add_widget(self.notice)
        pass
    
    def on_accepted_quest(self, obj):
        self.ids.available_quests.remove_widget(obj)
        self.ids.accepted_quests.add_widget(obj)

    def take_quest(self,notice):
        pass

class Notice(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def accept_quest(self,obj):
        pass

       
        

    def complete_quest(self,obj):
        pass