"""
CP1404 practicals - Practical 4
Cumulative total income program
"""


def main():
    """Start of program."""
    incomes = []
    number_of_months = int(input("How many months? "))
    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes.append(income)
    print_income_report(incomes)


def print_income_report(incomes):
    """Print income report based on monthly income."""
    print("\nIncome Report\n-------------")
    total = 0
    for index, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(index + 1, income, total))


main()
