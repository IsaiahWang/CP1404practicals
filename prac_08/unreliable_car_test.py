"""
CP1404/CP5632 Practical - Suggested Solution
UnreliableCar class tests
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""
    unreliable_car = UnreliableCar(name='ucar 1', fuel=1000, reliability=80)
    for i in range(10):
        unreliable_car.drive(distance=50)
        print(unreliable_car)
    # Unbound method
    UnreliableCar.drive(unreliable_car, 50)
    print(unreliable_car)


main()
