from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.core.window import Window
from Item import *
from kivy.uix.behaviors import ToggleButtonBehavior

class Shop(Screen):

    def __init__(self, player ,**kwargs):
        super().__init__(**kwargs)
        self.build_page()
        self.player = player

    def build_page(self):
        self.generate_items()
        item_types = ['Companion','Weapon','Helm']

        with open('itemDB_placeholder.json') as json_file:
            item_db = json.load(json_file)

        layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(len(item_types)):
            item_layout = GridLayout(cols=4, spacing=2, size_hint_y=None)
            lbl = Label(text=item_types[i])
            item_layout.add_widget(lbl)
            for j in item_db:
                current_obj = item_db.get(j)
                if current_obj['type'] == item_types[i]:
                    btn = ToggleButton(text=f"{current_obj['name']} \n"
                                            f"{current_obj['cost']} Golden Coins! \n",
                                       size_hint_y=None,
                                       height=100,
                                       group=item_types[i]
                                       )
                    btn.bind(on_release=self.event_popup(current_obj))
                    item_layout.add_widget(btn)
            layout.add_widget(item_layout)
        root = ScrollView(size_hint=(1,1), size=(Window.width, Window.height))
        root.add_widget(layout)
        self.add_widget(root)
        return self

    def event_popup(self, d):

        content = BoxLayout(orientation='vertical')
        label_box = BoxLayout()
        button_box = BoxLayout()
        content.add_widget(label_box)
        content.add_widget(button_box)

        label = Label(text=f"Name: {d['name']} \n"
                          f"Type:  {d['type']} \n"
                          f"Price: {d['cost']}")

        label_box.add_widget(label)

        def attempt_buy(obj):
            if self.player.golden_coins < d['cost']:
                print('insufficient funds :(')
            else:
                self.player.golden_coins -= d['cost']
                self.player.inventory[d['name']] = 1


        buy_button = Button(text='Buy!',size_hint=[1,0.2])
        buy_button.bind(on_release=attempt_buy)
        close_button = Button(text='Close me!',size_hint=[1,0.2])

        button_box.add_widget(buy_button)
        button_box.add_widget(close_button)

        popup = Popup(content=content, auto_dismiss=False)

        buy_button.bind(on_release=popup.dismiss)
        close_button.bind(on_release=popup.dismiss)
        def callback(instance):
            popup.open()

        return callback




    def generate_items(self):
        Item(1, 'Dog', 300, 'Companion')
        Item(2, 'Cat', 500, 'Companion')
        Item(3, 'Dragon', 800, 'Companion')
        Item(4, 'Knife', 550, 'Weapon')
        Item(5, 'Bow', 750, 'Weapon')
        Item(6, 'Sword', 650, 'Weapon')
        Item(7, 'Leather helm', 1200, 'Helm')
        Item(8, 'Steel helm', 1500, 'Helm')
        Item(9, 'Wizard hat', 1600, 'Helm')