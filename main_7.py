import os
filename = input("Please write a filename:");

basename, extension = os.path.splitext(filename)
print("Basename:",basename)
print("Extension:",extension)