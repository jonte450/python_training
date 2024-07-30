import os
from datetime import datetime

def sort_files_by_date(directory):
    # List all files in the given directory
    files = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    # Get the modification time for each file
    files_with_dates = [(file, os.path.getmtime(file)) for file in files]

    # Sort files by modification date
    sorted_files_with_dates = sorted(files_with_dates, key=lambda x: x[1])

    # Convert timestamps to readable format and return sorted list
    sorted_files = [(file, datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')) for file, mtime in sorted_files_with_dates]

    return sorted_files

# Example usage
directory = './'  # Replace with your directory path
sorted_files = sort_files_by_date(directory)
for file, date in sorted_files:
    print(f"{file}: {date}")
