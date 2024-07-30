def parse_string(value):
    try:
        # Try to convert the string to an integer
        result = int(value)
        return result
    except ValueError:
        try:
            # If it fails, try to convert the string to a float
            result = float(value)
            return result
        except ValueError:
            # If both conversions fail, raise an exception
            raise ValueError(f"Cannot parse '{value}' to an integer or float")

# Example usage
test_values = ["42", "3.14", "not_a_number"]

for value in test_values:
    try:
        parsed_value = parse_string(value)
        print(f"The parsed value of '{value}' is {parsed_value} (type: {type(parsed_value)})")
    except ValueError as e:
        print(e)
