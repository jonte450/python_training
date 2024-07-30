# Import the 'os.path' and 'time' modules to work with file system paths and timestamps.
import os.path, time

# Print the last modified timestamp of the file "test.txt" in a human-readable format.
print("Last modified: %s" % time.ctime(os.path.getmtime("64.py")))

# Print the creation timestamp of the file "test.txt" in a human-readable format.
print("Created: %s" % time.ctime(os.path.getctime("64.py")))

