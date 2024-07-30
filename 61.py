def convert_distance(feet):
    inches = feet * 12
    yards = feet / 3.0  # or feet // 3 for integer division
    miles = feet / 5280.0  # or feet // 5280 for integer division
    return inches, yards, miles

# Example usage
feet_distance = 100
inches, yards, miles = convert_distance(feet_distance)
print(f"{feet_distance} feet is equal to:")
print(f"{inches} inches")
print(f"{yards} yards")
print(f"{miles} miles")
