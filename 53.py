import os

home_dir = os.getenv('HOME')

print(f"Home directory: {home_dir}")

all_env = os.environ
print("\nAll environment variables:")
for key, value in all_env.items():
    print(f"{key}: {value}")
    