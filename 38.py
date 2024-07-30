def solve_expression(x, y):
    result = (x + y) * (x + y)
    return result

# Accepting two numbers from the user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Compute the result
result = solve_expression(x, y)

# Print the result
print(f"The result of ({x} + {y}) * ({x} + {y}) is: {result}")
