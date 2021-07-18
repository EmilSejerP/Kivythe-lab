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

    def scan_accepted_quests(self): ##not implemented. instead done on attempted quest completion
        return True

class Quest(Screen):
    def __init__(self, player, **kwargs):
        super().__init__(**kwargs)
        self.quest_tracker = QuestTracker() #init quest tracker that keeps track of progress

        self.notice = Notice(player)
        self.notice.text = "place 2 workout hours this week. On complete +2 str." 
        self.notice.bind(on_release=self.on_accepted_quest)
        self.notice.bonus_to_str = 2 #the bonuses and requirements for the tasks need to be set manually
        self.ids.available_quests.add_widget(self.notice) #add the notice to the available tasks in the app
       
        self.quest_tracker.accepted_quests.append(self.notice) #not implemented
    
    def on_accepted_quest(self, obj): ##when we press accept quest in app:
        self.ids.available_quests.remove_widget(obj) ##we remove it from the list of available quests
        self.ids.accepted_quests.add_widget(obj) #and move it to the accepted quest pool.
        obj.unbind(on_release=self.on_accepted_quest) #we unbind the accept quest command
        obj.bind(on_release=self.on_completed_quest) #and bind the complete quest command instead.
        print("accepted quest: ", obj)

    def on_completed_quest(self,obj): #if the player meets the requirements set for the task in quest tracker
        if obj.requirement_int >= self.quest_tracker.time_spent_int and obj.requirement_str >= self.quest_tracker.time_spent_str and obj.requirement_end >= self.quest_tracker.time_spent_end and obj.requirement_spt >= self.quest_tracker.time_spent_spt: #spaghetti.
            self.ids.accepted_quests.remove_widget(obj) #we remove the notice from the board 
            self.ids.available_quests.remove_widget(obj) #
            obj.complete_quest(obj) #and give the player the bonuses for completing the task.
            
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
        self.player.read_from_json()
        self.player.str += self.bonus_to_str
        self.player.int += self.bonus_to_int
        self.player.spt += self.bonus_to_spt
        self.player.end += self.bonus_to_end
        self.player.write_to_json()
        print("Quest completed.")
        ##popup?
     
    
