from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class QuestTracker:
    def __init__(self, *args, **kwargs):
        self.time_spent_str = 0
        self.time_spent_spt = 0
        self.time_spent_end = 0
        self.time_spent_int = 0
        self.accepted_quests = []

    def scan_accepted_quests(self):
        return True

class Quest(Screen):
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.quest_tracker = QuestTracker()

        self.notice = Notice(player)
        self.notice.text = "place 2 workout hours this week. On complete +2 str." 
        self.notice.bind(on_release=self.on_accepted_quest)
        self.notice.bonus_to_str = 2
        self.ids.available_quests.add_widget(self.notice)
       
        self.quest_tracker.accepted_quests.append(self.notice)
    
    def on_accepted_quest(self, obj):
        self.ids.available_quests.remove_widget(obj)
        self.ids.accepted_quests.add_widget(obj)
        obj.unbind(on_release=self.on_accepted_quest)
        obj.bind(on_release=self.on_completed_quest)
        print("accepted quest: ", obj)

    def on_completed_quest(self,obj):
        if obj.requirement_int >= self.quest_tracker.time_spent_int and obj.requirement_str >= self.quest_tracker.time_spent_str and obj.requirement_end >= self.quest_tracker.time_spent_end and obj.requirement_spt >= self.quest_tracker.time_spent_spt: #spaghetti.
            self.ids.accepted_quests.remove_widget(obj)
            self.ids.available_quests.remove_widget(obj)
            obj.complete_quest(obj)
            
            print("removed widget, and completed quest: ", obj)


    def remove_obj(self,obj):

        self.ids.accepted_quests.remove_widget(obj)
        self.ids.available_quests.remove_widget(obj)

        print("removed widget ", obj)

class Notice(Button):
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.bonus_to_int = 0
        self.bonus_to_str = 0
        self.bonus_to_end = 0
        self.bonus_to_spt = 0
        self.requirement_int = 0 #hours spent on the given task
        self.requirement_str = 0
        self.requirement_end = 0
        self.requirement_spt = 0
        self.player = player
        pass 

    def complete_quest(self,obj):

        self.player.str += self.bonus_to_str
        self.player.int += self.bonus_to_int
        self.player.spt += self.bonus_to_spt
        self.player.end += self.bonus_to_end

        print("Quest completed.")
        ##popup?
     
    
