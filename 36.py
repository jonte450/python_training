def add(obj1, obj2):
    if isinstance(obj1, int) and isinstance(obj2, int):
        return obj1 + obj2
    else:
        return "Both objects must be integers."
    


print(add(10, 20))     # Valid: Both inputs are integers, and it returns the sum.
print(add(10, 20.23))  # Invalid: One of the inputs is a float, so it returns an error message.
print(add('5', 6))     # Invalid: One of the inputs is a string, so it returns an error message.
print(add('5', '6'))