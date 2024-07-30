def height_feet_inches_to_cm(feet, inches):
    # 1 foot = 30.48 cm
    # 1 inch = 2.54 cm
    total_inches = feet * 12 + inches
    height_cm = total_inches * 2.54
    return height_cm

# Example usage
feet = 5
inches = 3
height_cm = height_feet_inches_to_cm(feet, inches)
print(f"{feet} feet {inches} inches is equal to {height_cm:.2f} centimeters")
