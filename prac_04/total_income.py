"""
CP1404/CP5632 Practical
Cumulative total income program
"""


def main():
    """main function"""
    incomes = []
    month_number = int(input("How many months? "))
    for month in range(1, month_number + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    print_income_report(incomes)


def print_income_report(incomes):
    """Print income report based on monthly income"""
    print("\nIncome Report\n-------------")
    total = 0
    for index, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(index + 1, income, total))


main()