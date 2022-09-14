"""
CP1404/CP5632 Practical
Sort files based on extension
"""
import os
import shutil


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir('FilesToSort')
    directory_names = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        directory_name = filename.split('.')[1]
        # LBYL
        if directory_name not in directory_names:
            directory_names.append(directory_name)
            os.mkdir(directory_name)
        shutil.move(filename, directory_name + '/' + filename)


main()
