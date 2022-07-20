import random


def main():
    """Main function"""
    # out_file = open('temps_input.txt', 'w')
    # for i in range(15):
    #     print(random.uniform(-200, 200), file=out_file)
    # out_file.close()
    in_file= open('temps_input.txt', 'r')
    out_file= open('temps_output.txt', 'w')
    for line in in_file.readlines():
        celsius = convert_fahrenheit_to_celsius(float(line))
        print(celsius, file=out_file)


def convert_fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()
