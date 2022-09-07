"""
CP1404/CP5632 Practical
SilverServiceTaxi class tests
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    silver_service_taxi = SilverServiceTaxi(name='Silver 1', fuel=1000, fanciness=2)
    print(silver_service_taxi.fuel)
    silver_service_taxi.drive(18)
    print(silver_service_taxi.get_fare())
    print(silver_service_taxi)


main()
