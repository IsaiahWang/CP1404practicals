"""
CP1404 practicals - Practical 2
Capitalist conrad program
"""
import random

MAX_PRICE = 1000
MIN_PRICE = 0.01
MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
OUTPUT_FILE = 'stock_price.txt'


def determine_trend():
    if random.randint(1, 2) == 1:
        return True  # price increase
    return False  # price decrease


# determine price increase ratio
def determine_increase_ratio():
    return random.uniform(0, MAX_INCREASE)


# determine price decrease ratio
def determine_decrease_ratio():
    return random.uniform(-MAX_DECREASE, 0)


price = 10
out_file = open(OUTPUT_FILE, 'w')
# print('Starting price: ${:.2f}'.format(price))
print(f'Starting price: ${price:,.2f}', file=out_file)
day_count = 1
while MAX_PRICE >= price >= MIN_PRICE:
    if determine_trend():
        price *= 1 + determine_increase_ratio()
    else:
        price *= 1 + determine_decrease_ratio()
    # print('On day {} price is: ${:.2f}'.format(day_count,price), out_file)
    print(f'On day {day_count} price is: ${price:,.2f}', file=out_file)
    day_count += 1
out_file.close()
