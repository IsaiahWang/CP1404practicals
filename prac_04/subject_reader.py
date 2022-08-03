"""
CP1404 practicals - Practical 4
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Start of program."""
    data = get_data()
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def print_subject_details(data):
    """Display data in a given format."""
    for subject_data in data:
        # print(f'{subject_data[0]} is taught by {subject_data[1]:12} and has {subject_data[2]:3} student')
        print('{} is taught by {:12} and has {:3} student'.format(*subject_data))


main()
