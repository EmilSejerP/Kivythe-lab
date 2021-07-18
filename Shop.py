from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from Item import *
class Shop(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_page()

    def build_page(self):
        self.generate_items()
        item_types = ['Companion','Weapon','Helmet','Item1','Item2','Item3','Item4']

        with open('itemDB_placeholder.json') as json_file:
            item_db = json.load(json_file)


        shop_layout = GridLayout(cols=4,spacing=2, size_hint_y=None)
        shop_layout.bind(minimum_height=shop_layout.setter('height'))
        for i in range(len(item_types)):
            lbl = Label(text=item_types[i])
            shop_layout.add_widget(lbl)
            for j in range(3):
                btn = ToggleButton(text=str(i + 1), size_hint_y=None, height=100, group=item_types[i])
                shop_layout.add_widget(btn)
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(shop_layout)
        self.add_widget(root)
    pass

    def generate_items(self):
        Item(1, 'Dog', 300, 'Companion')
        Item(2, 'Cat', 500, 'Companion')
        Item(3, 'Dragon', 800, 'Companion')