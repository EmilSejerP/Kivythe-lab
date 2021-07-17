from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from EventObject import *
from kivy.app import App


class NewEventPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()

    def create_page(self):
        box_layout = BoxLayout(orientation="vertical")
        box_layout_name = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_type = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_time = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])

        box_layout.add_widget(box_layout_name)
        box_layout.add_widget(box_layout_type)
        box_layout.add_widget(box_layout_time)

        name_label = Label(text="Give your Event a name: ", color=(0, 0, 0))
        type_label = Label(text="Which skill does this imrpove?", color=(0, 0, 0))
        time_label = Label(text="For how long?", color=(0, 0, 0))

        box_layout_name.add_widget(name_label)
        box_layout_type.add_widget(type_label)
        box_layout_time.add_widget(time_label)

        skill_lst = ['Strength', 'Endurance', 'Intelligence', 'Spirit']

        dropdown = DropDown()
        for index in range(4):
            btn = Button(text=f'{skill_lst[index]}', size_hint_y=None, height=20)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        mainbutton = Button(text='Choose skill', size_hint=(None, None), halign="center", valign="top")
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        text_field_name = TextInput()
        self.ids['text_field_name'] = text_field_name

        commit_button = Button(text="Commit Event")
        commit_button.bind(on_release=self.new_event)

        box_layout_type.add_widget(mainbutton)
        box_layout_type.add_widget(dropdown)
        box_layout_name.add_widget(text_field_name)
        box_layout_time.add_widget(commit_button)

        self.add_widget(box_layout)
        return self

    def new_event(self,obj):
        name = self.ids['text_field_name'].text
        event_object = EventObject(name, 'self.dropdown.text', 'mon', 12, 13)
        event_object.write_to_json()
