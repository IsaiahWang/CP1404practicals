"""
CP1404/CP5632 Practical
Test taxi
"""
from prac_08.taxi import Taxi


def main():
    """Test Taxi class."""
    taxi = Taxi(name='Pirus 1', fuel=100)
    taxi.drive(distance=40)
    print('Taxi details')
    print(taxi)
    print('Current fare')
    print(taxi.get_fare())
    taxi.start_fare()
    taxi.drive(distance=100)
    print('Taxi details')
    print(taxi)
    print('Current fare')
    print(taxi.get_fare())


main()
