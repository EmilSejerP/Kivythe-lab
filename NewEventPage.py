from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

class NewEventPage(Screen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def create_page(self):
        box_layout = BoxLayout(orientation="horizontal")
        box_layout_labels = BoxLayout(orientation="vertical")
        box_layout_fields = BoxLayout(orientation="vertical")
        box_layout.add_widget(box_layout_labels)
        box_layout.add_widget(box_layout_fields)

        self.add_widget(box_layout)
        return self

