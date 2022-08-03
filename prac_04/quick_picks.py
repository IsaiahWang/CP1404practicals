"""
CP1404 practicals - Practical 4
Quick pick program
"""

import random

LINE_NUMBER = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Start of program."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        numbers = []
        while len(numbers) < 6:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()
        print(" ".join("{:2}".format(number) for number in numbers))


main()
