"""
CP1404/CP5632 Practical
Convert miles to km kivy program
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class ConvertMilesToKM(App):
    """Kivy App for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.root = Builder.load_file('convert_miles_km.kv')

    def handle_increment(self, value, increment):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        try:
            temp = float(value) + increment
        except ValueError:
            temp = 0.0 + increment
        self.root.ids.input_number.text = str(temp)

    def convert_miles_to_km(self, miles):
        """Convert miles tp km."""
        try:
            temp = float(miles) * FACTOR_MILES_TO_KM
        except ValueError:
            temp = 0.0
        self.output_km = str(temp)


ConvertMilesToKM().run()
