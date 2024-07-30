import os

def check_file_exists(file_path):
    return os.path.exists(file_path)

# Accepting the file path from the user
file_path = input("Enter the file path: ")

# Check if the file exists
if check_file_exists(file_path):
    print("The file exists.")
else:
    print("The file does not exist.")
