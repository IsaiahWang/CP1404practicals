import random


def main():
    score_number = int(input('Please input number of scores: '))
    out_file = open('results.txt', 'w')
    for i in range(score_number):
        random_score = random.randint(0, 100)
        out_file.write(f'{random_score} is {determine_result(random_score)}\n')
    out_file.close()


def determine_result(score):
    """determine result based on score"""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
