"""
CP1404 practicals - Practical 3
Broken program to determine score status
"""
import random


def main():
    """Start of program."""
    score = float(input("Enter score: "))
    print(determine_result(score))
    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(f'Random score is {random_score} and random result is {random_result}')


def determine_result(score):
    """Determine result based on score."""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
