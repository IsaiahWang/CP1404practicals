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
    """determine trend of the stock"""
    if random.randint(1, 2) == 1:
        return True  # price increase
    return False  # price decrease


def determine_increase_ratio():
    """determine price increase ratio"""
    return random.uniform(0, MAX_INCREASE)


def determine_decrease_ratio():
    """determine price decrease ratio"""
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
