"""
CP1404 practicals - Practical 2
Exception demo
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print('Denominator should not be 0')
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")

'''
1. When user input is not integer, ValueError occurs
2. When denominator is 0, ZeroDivisionError occurs
'''
