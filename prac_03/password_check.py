MIN_LENGTH = 8


def main():
    """Function docstring"""
    password = get_password()
    while len(password) < MIN_LENGTH:
        print('Too short!')
        password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    print('*' * len(password))


def get_password():
    password = input('Please input your password: ')
    return password


main()
