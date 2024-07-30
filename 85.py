import os

def check_path(path):
    if os.path.isdir(path):
        print(f"{path} is a directory.")
    elif os.path.isfile(path):
        print(f"{path} is a file")
    else:
        print(f"{path} does not exist and is not a file or a directory")

check = input("Please type a path: ")
check_path(check)

