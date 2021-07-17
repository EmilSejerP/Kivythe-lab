from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.slider import Slider


class NewEventPage(Screen):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def create_page(self):
        box_layout = BoxLayout(orientation="vertical")
        box_layout_name = BoxLayout(orientation="horizontal",size_hint=(0.5,1))
        box_layout_type = BoxLayout(orientation="horizontal")
        box_layout_time = BoxLayout(orientation="horizontal")

        box_layout.add_widget(box_layout_name)
        box_layout.add_widget(box_layout_type)
        box_layout.add_widget(box_layout_time)

        name_label = Label(text = "Give your Event a name: ")
        type_label = Label(text = "Which skill does this imrpove?")
        time_label = Label(text = "For how long?")

        box_layout_name.add_widget(name_label)
        box_layout_type.add_widget(type_label)
        box_layout_time.add_widget(time_label)

        skill_lst = ['Strength','Endurance','Intelligence','Spirit']

        dropdown = DropDown()
        for index in range(4):
            btn = Button(text=f'{skill_lst[index]}', size_hint_y=None, height=20)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        mainbutton = Button(text='Choose skill', size_hint=(None, None),halign="center",valign="top")
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        btn1 = Button(text="Im next field",size_hint=[1, 0.15])
        time_slider = Slider(min=1,max=24,orientation = 'horizontal')

        box_layout_type.add_widget(mainbutton)
        box_layout_type.add_widget(dropdown)
        box_layout_name.add_widget(btn1)
        box_layout_time.add_widget(time_slider)

        self.add_widget(box_layout)
        return self

