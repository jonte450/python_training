def print_without_newline_or_space(*args):
    # Use end='' to avoid newlines and spaces between prints
    for arg in args:
        print(arg, end='')
    # Ensure the buffer is flushed to show the output immediately
    print(flush=True)

# Example usage
print_without_newline_or_space('H', 'e', 'l', 'l', 'o')
