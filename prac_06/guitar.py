"""
CP1404/CP5632 Practical
Guitar class
"""
import datetime
CURRENT_YEAR = datetime.datetime.now().year
VINTAGE_AGE = 50


class Guitar:
    """Represent a Car object."""

    def __init__(self, name='', year=0, cost=0):
        """Construct a Guitar object."""
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Return a string representation if a Guitar."""
        return f'{self.name} ({self.year}) : ${self.cost:,.2f}'

    def get_age(self):
        """Get the age of a guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare two guitars by their ages"""
        return self.year < other.year
