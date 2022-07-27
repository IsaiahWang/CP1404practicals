MIN_LENGTH = 8


def main():
    """Start of program."""
    password = get_password(MIN_LENGTH)
    while len(password) < MIN_LENGTH:
        print('Too short!')
        password = get_password()
    print_asterisk(password)


def print_asterisk(password):
    """Print the same number of asterisks as the length of password."""
    print('*' * len(password))


def get_password(minimum_length):
    """Get password from user input and make sure it meets the minimum length."""
    password = input(f'Please input your password (at least {minimum_length} characters): ')
    while len(password) < minimum_length:
        print('Password is too short!')
        password = input(f'Please input your password (at least {minimum_length} characters): ')
    return password


main()
