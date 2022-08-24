"""
CP1404/CP5632 Practical
Guitar program.
"""
from prac_06.guitar import Guitar


def main():
    """Start a program."""
    print('My guitars!')
    name = input('Name: ')
    guitars = []
    while name != '':
        year = input('Year: ')
        cost = input('Cost: $')
        guitar = Guitar(name=name, year=year, cost=cost)
        guitars.append(guitar)
        print(guitar, 'added.')
        print()
        name = input('Name: ')
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        guitars.sort()
        # guitars.sort(key=lambda x: x.year)
        # guitars.sort(key=operator.attrgetter('year'))
        print('These are my guitars:')
        for i, guitar in enumerate(guitars):
            print(
                f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{' (vintage)' if guitar.is_vintage() else ''}")
    else:
        print('No guitars!')


main()
