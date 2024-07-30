def count_character_occurrences(input_string, character):
    """
    Counts the number of occurrences of a specific character in a string.
    
    Parameters:
    input_string (str): The string in which to count occurrences.
    character (str): The character whose occurrences are to be counted.
    
    Returns:
    int: The number of occurrences of the character.
    """
    if len(character) != 1:
        raise ValueError("The character parameter must be a single character.")
    
    return input_string.count(character)

def main():
    # Get input from the user
    input_string = input("Enter the string: ")
    character = input("Enter the character to count: ")
    
    # Ensure that the user inputs only a single character
    if len(character) != 1:
        print("Error: Please enter exactly one character.")
        return
    
    # Count occurrences of the character
    count = count_character_occurrences(input_string, character)
    
    # Print the result
    print(f"The character '{character}' occurs {count} times in the string.")

if __name__ == "__main__":
    main()
