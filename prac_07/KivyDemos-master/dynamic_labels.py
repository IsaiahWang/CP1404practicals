"""
CP1404/CP5632 Practical
Dynamic Labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicNameLabels(App):
    """Kivy app for dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # list of names
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Haidong Wang", "San Zhang"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_name_labels()
        return self.root

    def create_name_labels(self):
        """Create buttons from name list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicNameLabels().run()