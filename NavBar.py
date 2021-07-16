"""
#create upper menu
box_layout = BoxLayout(size_hint=[1,0.1])
box_layout.add_widget(Button(text="Calendar"))
box_layout.add_widget(Button(text="Character"))
box_layout.add_widget(Button(text="Journal"))
box_layout.add_widget(Button(text="Shop"))

main_box.add_widget(box_layout)
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button




class NavBar(BoxLayout):

    def __init__(self,sm):
        self.sm = sm
        print("biggos")

    def get_nav(self):

        calendar_btn = Button(text="Calendar")
        character_btn = Button(text="Character")
        journal_btn = Button(text="Journal")
        quest_btn = Button(text="Quests")
        shop_btn = Button(text="Shop")

        calendar_btn.bind(on_release=self.callback())



    def callback(self,instance,arg):
        self.sm.switch_to(arg)