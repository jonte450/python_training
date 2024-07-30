# Define a function 'sum_three' that takes three integer inputs: x, y, and z.
def sum_three(x, y, z):
    # Check if any of the two input values are equal. If so, set 'sum' to 0.
    if x == y or y == z or x == z:
        sum = 0
    else:
        # If all three input values are distinct, calculate the sum of x, y, and z.
        sum = x + y + z
    # Return the calculated sum.
    return sum

# Test the 'sum_three' function with different sets of input values and print the results.
print(sum_three(2, 1, 2))
print(sum_three(3, 2, 2))
print(sum_three(2, 2, 2))
print(sum_three(1, 2, 3))