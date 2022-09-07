"""
CP1404/CP5632 Practical
Box Layout Demo
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box Layout App for greeting."""

    def build(self):
        """Build the app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the name user inputs."""
        print('greet')
        self.root.ids.output_label.text = 'Hello ' + self.root.ids.input_name.text

    def handle_clear(self):
        """Clear both the input and output."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
