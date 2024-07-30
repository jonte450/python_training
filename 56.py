import shutil

def console_size():
    size = shutil.get_terminal_size()
    return size.columns , size.lines


width, height = console_size()
print(f"Console width: {width} columns")
print(f"Console height: {height} lines")