import os



file = input("Enter a file name: ")
print(f"The size is {file}: {os.path.getsize(file)} Bytes")
