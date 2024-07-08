def is_within_100(num):
    return abs(num - 1000) <= 100 or abs(num - 2000) <= 100

# Test the function
num1 = 900
num2 = 1050
num3 = 1900

print(num1, "is within 100 of either 1000 or 2000:", is_within_100(num1))
print(num2, "is within 100 of either 1000 or 2000:", is_within_100(num2))
print(num3, "is within 100 of either 1000 or 2000:", is_within_100(num3))
