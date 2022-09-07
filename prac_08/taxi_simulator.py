"""
CP1404/CP5632 Practical
Taxi simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """Start of taxi simulator program."""
    total_bill = 0
    prius = Taxi(name='Pirus', fuel=100)
    limo = SilverServiceTaxi(name='Limo', fuel=100, fanciness=2)
    hummer = SilverServiceTaxi(name='Hummer', fuel=200, fanciness=4)
    taxis = [prius, limo, hummer]
    print("Let's drive!")
    print(MENU)
    option = input('>>> ').lower()
    while option != 'q':
        if option == 'c':
            print('Taxis available: ')
            display_taxis(taxis)
            taxi_option = int(input('Choose taxi: '))
            # Error check for correct taxi index
            try:
                current_taxi = taxis[taxi_option]
            except IndexError:
                print('Invalid taxi option')
        elif option == 'd':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input('Drive how far? '))
                current_taxi.drive(drive_distance)
                taxi_fare = current_taxi.get_fare()
                print(f'Your {current_taxi.name} trip cost you ${taxi_fare}')
                total_bill += taxi_fare
            else:
                print('Please choose a taxi first!')
        else:
            print('Invalid Option!')
        print(f'Bill to date: ${total_bill:.2f}')
        print(MENU)
        option = input('>>> ').lower()
    print(f'Total trip cost: ${total_bill:.2f}')
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of taxis."""
    for index, taxi in enumerate(taxis):
        print(str(index) + ' - ' + str(taxi))


main()
