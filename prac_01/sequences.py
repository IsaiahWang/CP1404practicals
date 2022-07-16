"""
CP1404 practicals - Practical 1
Sequences program
"""
x = int(input('Enter an integer as x: '))
y = int(input('Enter an integer greater than x as y: '))
print('(e)Show the even numbers from x to y\n'
      '(o)Show the odd numbers from x to y\n'
      '(s)Show the squares from x to y\n'
      '(q)Exit the program')
choice = input('>>> ').lower()
while choice != 'q':
    if choice == 'e':
        for i in range(x if x % 2 == 0 else x+1, y+1, 2):
            print(i, end=' ')
    elif choice == 'o':
        for i in range(x if x % 2 == 1 else x+1, y+1, 2):
            print(i, end=' ')
    elif choice == 's':
        for i in range(x,y+1):
            print(i, end=' ')
    else:
        print('Invalid Choice')
    print()
    print('(e)Show the even numbers from x to y\n'
          '(o)Show the odd numbers from x to y\n'
          '(s)Show the squares from x to y\n'
          '(q)Exit the program')
    choice = input('>>> ').lower()
print('Finished.')