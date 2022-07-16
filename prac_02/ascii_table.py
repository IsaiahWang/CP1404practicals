MIN_BOUND = 33
MAX_BOUND = 127
char = input('Enter a character: ')
print(f'The ASCII code for g is {ord(char)}')
number = int(input(f'Enter a number between {MIN_BOUND} and {MAX_BOUND}: '))
while number < 33 or number > 127:
    print('Wrong value!')
    number = int(input(f'Enter a number between {MIN_BOUND} and {MAX_BOUND}: '))
print(f'The character for 100 is {chr(number)}')
for i in range(33,128):
    print('{:3} {}'.format(i,chr(i)))
