import sys

def print_to_stderr(message):
    print(message, file=sys.stderr)

# Example usage
print_to_stderr("This is an error message.")
