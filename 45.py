import subprocess

def call_external_command(command):
    try:
        # Run the external command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # Print the output and return code
        print("Output:")
        print(result.stdout)
        print("Error:")
        print(result.stderr)
        print(f"Return code: {result.returncode}")
    except subprocess.CalledProcessError as e:
        # Print the error if the command fails
        print(f"Command failed with return code {e.returncode}")
        print("Error output:")
        print(e.stderr)

if __name__ == "__main__":
    # Example: call the 'ls' command (on Unix-like systems) or 'dir' command (on Windows)
    command = ["ls"]  # For Unix-like systems
    # command = ["dir"]  # For Windows systems, uncomment this line and comment the above line
    
    call_external_command(command)
