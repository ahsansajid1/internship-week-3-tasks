import os  # To work with the operating system

# List all items in the current directory
for file in os.listdir():
    # Check if the item is a Python file
    if file.endswith(".py"):
        size = os.path.getsize(file)  # Get size in bytes
        print(f"{file} - {size} bytes")
