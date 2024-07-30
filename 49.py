import os

def list_files_in_directory(directory):
    try:
        # Get the list of all files and directories in the specified directory
        entries = os.listdir(directory)
        
        # Filter the list to include only files
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        
        return files
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
        return []
    except PermissionError:
        print(f"Permission denied to access the directory '{directory}'.")
        return []

# Example usage
directory_path = '.'  # Current directory
files = list_files_in_directory(directory_path)

if files:
    print("Files in directory:")
    for file in files:
        print(file)
else:
    print("No files found or error accessing the directory.")
