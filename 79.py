import sys

def obj_size(obj):
    return sys.getsizeof(obj)


obj = input("Write something to get the bytes: ")

print(f"The bytes of the value is: {obj_size(obj)}")

