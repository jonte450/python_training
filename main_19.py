def add_is_to_string(string):
    if string.startswith("Is"):
        return string
    else:
        return "Is" + string

# Test the function
given_string1 = "apple"
given_string2 = "Is banana"

new_string1 = add_is_to_string(given_string1)
new_string2 = add_is_to_string(given_string2)

print("Original string:", given_string1)
print("Modified string:", new_string1)

print("\nOriginal string:", given_string2)
print("Modified string:", new_string2)
