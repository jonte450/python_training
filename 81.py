def concatenate_strings(strings):
    return ''.join(strings)

def main():
    # Get the number of strings to concatenate
    n = int(input("Enter the number of strings to concatenate: "))
    
    # Get `n` strings from the user
    strings = []
    for i in range(n):
        string = input(f"Enter string {i + 1}: ")
        strings.append(string)
    
    # Concatenate the strings
    result = concatenate_strings(strings)
    
    # Print the result
    print("Concatenated string:", result)

if __name__ == "__main__":
    main()
