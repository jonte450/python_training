import math

def compute_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Accepting two positive integers from the user
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

# Compute the LCM
lcm = compute_lcm(num1, num2)

# Print the result
print(f"The least common multiple (LCM) of {num1} and {num2} is {lcm}")
