"""
CP1404 Practical 5
Email to name dictionary
"""


def main():
    """Start of program."""
    email_to_name = {}
    email = input('Email: ')
    while email != '':
        name_str = email.split('@')[0]
        name_list = name_str.split('.')
        name = ' '.join(name_list).title()
        is_name_correct = input(f'Is your name {name}? (Y/n) ').lower()
        if is_name_correct != 'y' and is_name_correct != '':
            name = input('Name: ')
        email_to_name[email] = name
        email = input('Email: ')
    for item in email_to_name.items():
        print(f'{item[1]} ({item[0]})')


main()