from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


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

    def switch_to(self,arg):
        def callback(instance):
            self.sm.switch_to(arg)
        return callback