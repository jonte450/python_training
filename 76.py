import sys

def main():
    # Get the name of the script
    script_name = sys.argv[0]
    
    # Get the number of arguments (excluding the script name)
    num_args = len(sys.argv) - 1
    
    # Get the arguments (excluding the script name)
    arguments = sys.argv[1:]
    
    # Print the script name, number of arguments, and the arguments
    print(f"Script name: {script_name}")
    print(f"Number of arguments: {num_args}")
    print(f"Arguments: {arguments}")

if __name__ == "__main__":
    main()
