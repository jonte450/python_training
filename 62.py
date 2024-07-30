def convert_to_seconds(days=0, hours=0, minutes=0, seconds=0):
    total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
    return total_seconds

# Example usage
days = 4
hours = 5
minutes = 20
seconds = 10

total_seconds = convert_to_seconds(days, hours, minutes, seconds)
print(f"{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds is equal to:")
print(f"{total_seconds} seconds")
