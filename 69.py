def sort_three_numbers(a, b, c):
    # Calculate the minimum, maximum, and the remaining number
    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = (a + b + c) - (smallest + largest)
    
    return smallest, middle, largest

# Example usage
a, b, c = 3, 1, 2
sorted_numbers = sort_three_numbers(a, b, c)
print(f"The sorted numbers are: {sorted_numbers}")
