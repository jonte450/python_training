def is_vowel(str):
    return str.lower() in "aieou"



print(is_vowel('c'))  # Output: False (character 'c' is not a vowel)
print(is_vowel('e'))  # Output: True (character 'e' is a vowel)