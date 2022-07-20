MIN_LENGTH = 8
password = input('Please input your password: ')
while len(password) < MIN_LENGTH:
    print('Too short!')
    password = input('Please input your password: ')
print('*' * len(password))