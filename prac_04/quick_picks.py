import random

LINE_NUMBER = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    pick_number = int(input('How many quick picks? '))
    for i in range(pick_number):
        numbers = []
        while len(numbers) < 6:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if not number in numbers:
                numbers.append(number)
        numbers.sort()
        for number in numbers:
            print('{:2}'.format(number), end=' ')
        print()


main()
