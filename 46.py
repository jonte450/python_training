import os


def curr_path():
    file_path = os.path.abspath(__file__)
    return file_path


if __name__ == "__main__":
    cp = curr_path()

    print(cp)