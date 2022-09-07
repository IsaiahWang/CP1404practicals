"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability."""
        random_number = random.randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            print('Fail to drive!')
        return distance_driven
