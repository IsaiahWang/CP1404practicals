"""
CP1404 practicals - Practical 4
List exercises
"""


def main():
    """Start of program."""
    # 1. Numbers stuff
    numbers = []
    for i in range(5):
        number = int(input('Number: '))
        numbers.append(number)
    print(f'The first number is {numbers[0]}')
    print(f'The last number is {numbers[-1]}')
    print(f'The smallest number is {min(numbers)}')
    print(f'The largest number is {max(numbers)}')
    print(f'The average of the numbers is {sum(numbers) / len(numbers)}')
    # 2. Inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input('Please input your username: ')
    if username in usernames:
        print('Access granted')
    else:
        print('Access denied')


main()
