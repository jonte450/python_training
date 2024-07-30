import math

def calculate_hypotenuse(a, b):
    # Calculate hypotenuse using the Pythagorean theorem
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

# Example usage
side1 = 3
side2 = 4
hypotenuse = calculate_hypotenuse(side1, side2)
print(f"The hypotenuse of the right-angled triangle with sides {side1} and {side2} is: {hypotenuse:.2f}")
