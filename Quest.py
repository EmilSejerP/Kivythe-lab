from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class QuestTracker:
    def __init__(self, *args, **kwargs):
        self.time_spent_str = 0
        self.time_spent_spt = 0
        self.time_spent_end = 0
        self.time_spent_int = 0
        accepted_quests = []

    def scan_accepted_quests(self):
        pass

class Quest(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.notice = Notice()

        self.notice.text = "place 2 workout hours this week. On complete +2 str." 

        self.notice.bind(on_release=self.on_accepted_quest)

        self.ids.available_quests.add_widget(self.notice)
        pass
    
    def on_accepted_quest(self, obj):
        self.ids.available_quests.remove_widget(obj)
        self.ids.accepted_quests.add_widget(obj)
        obj.bind(on_release=obj.complete_quest)

class Notice(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus_to_int = 0
        self.bonus_to_str = 0
        self.bonus_to_end = 0
        self.bonus_to_spt = 0
        self.requirement_int = 0
        self.requirement_str = 0
        self.requirement_end = 0
        self.requirement_spt = 0
        pass 

    def complete_quest(self,obj):
        self.parent.remove_widget(self)

        ##popup?
        del self
    
