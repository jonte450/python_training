import platform

# Get the OS name
os_name = platform.system()

# Get the platform information
platform_info = platform.platform()

# Get the OS release information
os_release = platform.release()

# Print the information
print(f"OS Name: {os_name}")
print(f"Platform Information: {platform_info}")
print(f"OS Release: {os_release}")
