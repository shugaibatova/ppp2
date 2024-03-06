# Write a Python program to list only directories, files and all directories, files in a specified path.
# Write a Python program to check for access to a specified path. Test the existence, readability, writability
#  and executability of the specified path
# Write a Python program to test whether a given path exists or not. If the path exist find the filename
#  and directory portion of the given path.
# Write a Python program to count the number of lines in a text file.
# Write a Python program to write a list to a file.
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# Write a Python program to copy the contents of a file to another file
# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def list_dir_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

example_path = r"C:\Users\User\Documents\uni\mpge"

directory_path = os.path.dirname(example_path)

print("List of directories and files in the specified directory:")
list_dir_and_files(directory_path)