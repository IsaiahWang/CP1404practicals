"""
CP1404/CP5632 Practical
Sort files based on extension and user categorisation
"""
import os
import shutil


def main():
    """Move files into where user wants to store them based on extension."""
    os.chdir('FilesToSort')
    file_type_to_directory_name = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split('.')[1]
        if file_type not in file_type_to_directory_name.keys():
            directory_name = input(f'What category would you like to sort {file_type} files into? ')
            file_type_to_directory_name[file_type] = directory_name
            try:
                os.mkdir(directory_name)
            except FileExistsError:
                pass
        directory_name = file_type_to_directory_name[file_type]
        shutil.move(filename, directory_name + '/' + filename)


main()
