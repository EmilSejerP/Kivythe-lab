from kivy.uix.screenmanager import Screen

class Shop(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """start_tid_layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        start_tid_layout.bind(minimum_height=start_tid_layout.setter('height'))
        for i in range(24):
            btn = ToggleButton(text=str(i + 1), size_hint_y=None, height=20, group='start_tid')
            start_tid_layout.add_widget(btn)

        root = ScrollView(size_hint=(1, None))
        root.add_widget(start_tid_layout)
        box_layout_time.add_widget(root)"""

    pass
