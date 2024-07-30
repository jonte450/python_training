import sys

def check_endian():
    if sys.byteorder == "little":
        print("The system is little-endian.")
    else:
        print("The system is big-endian.")


check_endian()