"""
CP1404/CP5632 Practical
SilverServiceTaxi class, derived from Taxi
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return (
            f'{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus '
            f'flagfall of ${self.flagfall:.2f} ')

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
