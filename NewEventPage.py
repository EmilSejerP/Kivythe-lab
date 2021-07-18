from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton

from EventObject import *
from kivy.app import App
from kivy.uix.scrollview import ScrollView


class NewEventPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = App.get_running_app()
        self.days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.create_page()

    def create_page(self):

        box_layout = BoxLayout(orientation="vertical")
        box_layout_name = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_type = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_day_labels = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_day = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])
        box_layout_time = BoxLayout(orientation="horizontal", padding=[20, 20, 20, 20])

        box_layout.add_widget(box_layout_name)
        box_layout.add_widget(box_layout_type)
        box_layout.add_widget(box_layout_day_labels)
        box_layout.add_widget(box_layout_day)
        box_layout.add_widget(box_layout_time)

        name_label = Label(text="Give your Event a name: ")
        type_label = Label(text="Which skill does this imrpove?")
        day_label = Label(text="What days?")
        time_label = Label(text="For how long?")

        box_layout_name.add_widget(name_label)
        box_layout_type.add_widget(type_label)
        box_layout_day.add_widget(day_label)
        box_layout_time.add_widget(time_label)

        skill_lst = ['Strength', 'Endurance', 'Intelligence', 'Spirit']

        type_dropdown = DropDown()
        for index in range(4):
            btn = Button(text=f'{skill_lst[index]}', size_hint_y=None, height=20)
            btn.bind(on_release=lambda btn: type_dropdown.select(btn.text))
            type_dropdown.add_widget(btn)
        mainbutton = Button(text='Choose skill', size_hint=(None, None), halign="center", valign="top")
        self.ids['mainbutton'] = mainbutton
        mainbutton.bind(on_release=type_dropdown.open)
        type_dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        text_field_name = TextInput()
        self.ids['text_field_name'] = text_field_name

        commit_button = Button(text="Commit Event")
        commit_button.bind(on_release=self.new_event)

        for day in self.days:
            label = Label(text=day)
            box_layout_day_labels.add_widget(label)
            check_box = CheckBox()
            self.ids[f'{day}'] = check_box
            box_layout_day.add_widget(check_box)

        box_layout_type.add_widget(mainbutton)
        box_layout_type.add_widget(type_dropdown)
        box_layout_name.add_widget(text_field_name)

        slut_tid_layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        slut_tid_layout.bind(minimum_height=slut_tid_layout.setter('height'))
        start_tid_layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        start_tid_layout.bind(minimum_height=start_tid_layout.setter('height'))

        for i in range(24):
            btn = ToggleButton(text=str(i+1),size_hint_y=None,height=20,group='start_tid')
            start_tid_layout.add_widget(btn)
            btn = ToggleButton(text=str(i + 1), size_hint_y=None, height=20,group='slut_tid')
            slut_tid_layout.add_widget(btn)

        root = ScrollView(size_hint=(1, None))
        root.add_widget(start_tid_layout)
        box_layout_time.add_widget(root)
        root1 = ScrollView(size_hint=(1, None))
        root1.add_widget(slut_tid_layout)
        box_layout_time.add_widget(root1)
        box_layout_time.add_widget(commit_button)

        self.add_widget(box_layout)
        return self

    def new_event(self,obj):
        start_tid = [i.text for i in ToggleButtonBehavior.get_widgets('start_tid') if i.state == 'down']
        slut_tid = [i.text for i in ToggleButtonBehavior.get_widgets('slut_tid') if i.state == 'down']
        if int(slut_tid[0]) - int(start_tid[0]) > 0:
            name = self.ids['text_field_name'].text
            type = self.ids['mainbutton'].text
            for day in self.days:
                if self.ids[day].active == True:
                    event_object = EventObject(f'{name}{day}{str(start_tid)}',name, type, day, start_tid, slut_tid)
                    event_object.write_to_json()
                else:
                    print('Error creating event: cannot create events that goes into the past')
