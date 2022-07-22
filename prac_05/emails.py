def main():
    name_email_dict = {}
    email = input('Email: ')
    while email != '':
        name_str = email.split('@')[0]
        name_list = name_str.split('.')
        blank = ' '
        name = blank.join(name_list).title()
        is_name_correct = input(f'Is your name {name}? (Y/n)').lower()
        if is_name_correct != 'y' and is_name_correct != '':
            name = input('Name: ')
        name_email_dict.update({email:name})
        email = input('Email: ')
    for item in name_email_dict.items():
        print(f'{item[1]} ({item[0]})')


main()