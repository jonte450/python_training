import platform

# Check the bit architecture of the Python interpreter
bit_architecture = platform.architecture()[0]

if bit_architecture == '32bit':
    print("Python interpreter is running in 32-bit mode.")
elif bit_architecture == '64bit':
    print("Python interpreter is running in 64-bit mode.")
else:
    print("Unknown bit architecture.")
