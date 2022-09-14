"""
CP1404/CP5632 Practical
Cleanup inconsistent song lyrics file names
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            filename = os.path.join(directory_name, filename)
            os.rename(filename, new_name)
            print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    file_name = filename.split('.')[0]
    file_type = filename.split('.')[1]
    file_name_list = list(file_name)
    for i in range(len(file_name_list) - 1):
        if file_name_list[i].islower() and file_name_list[i + 1].isupper():
            file_name_list.insert(i + 1, '_')
        if file_name_list[i] == ' ':
            file_name_list[i] = '_'
    new_file_name = ''.join(file_name_list).title()
    new_full_file_name = new_file_name + '.' + file_type.lower()
    return new_full_file_name


main()
