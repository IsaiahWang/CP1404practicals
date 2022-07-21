"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_list = get_data()
    print(data_list)
    print_subject_details(data_list)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        data.append(parts)
    input_file.close()
    return data


def print_subject_details(data_list):
    for data in data_list:
        print(f'{data[0]} is taught by {data[1]:12} and has {data[2]:>3} student')


main()