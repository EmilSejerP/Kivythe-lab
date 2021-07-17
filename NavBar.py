from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class NavBar(BoxLayout):

    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.__setattr__("size_hint",[1,0.1])
        self.sm = sm

    def main_navbar(self,lst):
        calendar_button = Button(text="Calendar")
        calendar_button.bind(on_release=self.switch_to(lst[0]))
        character_button = Button(text="Character")
        character_button.bind(on_release=self.switch_to(lst[1]))
        journal_button = Button(text="Journal")
        journal_button.bind(on_release=self.switch_to(lst[2]))
        quest_button = Button(text="Quest")
        quest_button.bind(on_release=self.switch_to(lst[3]))
        shop_button = Button(text="Shop")
        shop_button.bind(on_release=self.switch_to(lst[4]))

        self.add_widget(calendar_button)
        self.add_widget(character_button)
        self.add_widget(journal_button)
        self.add_widget(quest_button)
        self.add_widget(shop_button)

        return self

    def calender_navbar(self, page):
        box_layout = BoxLayout(size_hint=[1, 0.1])

        new_event_btn = Button(text="+", pos_hint={'right': 1}, size_hint=[0.15, 1])
        new_event_btn.bind(on_release=self.switch_to(page))

        box_layout.add_widget(Button(text="<", pos_hint={'left': 1}, size_hint=[0.15, 1]))
        box_layout.add_widget(Label(text="What week are we in?", pos_hint={'center': 1}))
        box_layout.add_widget(new_event_btn)
        box_layout.add_widget(Button(text=">", pos_hint={'right': 1}, size_hint=[0.15, 1]))
        return box_layout

    def switch_to(self,arg):
        def callback(instance):
            self.sm.switch_to(arg)
        return callback