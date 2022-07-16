"""
CP1404 practicals - Practical 1
Loops
"""
# print add numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# print numbers from 0 to 100 in 10s
for i in range(0, 101, 10):
    print(i, end=' ')
    # time.sleep(1)
print()

# print numbers from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# print number of stars that user inputs
number_of_starts = int(input('Number of stars: '))
for i in range(number_of_starts):
    print('*', end='')
print()

# print number of lines of increasing stars that user inputs
for i in range(number_of_starts):
    print('*' * (i+1))
print()