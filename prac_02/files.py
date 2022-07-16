"""
CP1404 practicals - Practical 2
Files
"""

# Program 1
name = input('Input your name: ')
with open('name.txt', 'w') as out_file:
    out_file.write(name)

# Program 2
in_file = open('name.txt', 'r')
read_name = in_file.read().strip()
print(f'Your name is {read_name}')
in_file.close()

# Program 2 using 'with'
with open('name.txt', 'r') as in_file:
    name = in_file.read().strip()
print(f'Your name is {read_name}')

# Program 3
number_file = open('numbers.txt', 'r')
total = 0
for i in range(2):
    number = int(number_file.readline())
    total += number
print(total)
number_file.close()

# Program 4
number_file = open('numbers.txt', 'r')
total = 0
for line in number_file:
    number = int(line)
    total += number
print(total)
number_file.close()

