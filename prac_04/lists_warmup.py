"""
CP1404 practicals - Practical 4
Lists "warm-up"
"""


def main():
    """Start of program."""
    numbers = [3, 1, 4, 1, 5, 9, 2]  # 3
    print(numbers[0])  # 3
    print(numbers[-1])  # 2
    print(numbers[3])  # 1
    print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
    print(numbers[3:4])  # [1]
    print(5 in numbers)  # True
    print(7 in numbers)  # False
    print('3' in numbers)  # False
    print(numbers + [6, 5, 3])  # [3, 1, 4, 5, 9, 2, 6, 5, 3]
    numbers[0] = 'ten'
    numbers[-1] = 1
    print(numbers[2:])
    print(9 in numbers)


main()
