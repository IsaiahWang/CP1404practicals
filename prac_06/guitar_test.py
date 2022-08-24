"""
CP1404/CP5632 Practical
Basic manual tests for Guitar class
"""
from prac_06.guitar import Guitar


def main():
    """Start of a program."""
    guitar_1 = Guitar(name='Gibson L-5 CES', year=1924)
    guitar_2 = Guitar(name='Another Guitar', year=2013)
    print(f'{guitar_1.name} get_Age() - Expected 98. Got {guitar_1.get_age()}')
    print(f'{guitar_2.name} get_Age() - Expected 9. Got {guitar_2.get_age()}')
    print(f'{guitar_1.name} is_vintage() - Expected True. Got {guitar_1.is_vintage()}')
    print(f'{guitar_2.name} is_vintage() - Expected False. Got {guitar_2.is_vintage()}')


main()
