import os

file = "sample.txt"

try:
    os.remove(file)
    print(f"{file} has been deleted successfully")
except FileNotFoundError:
    print(f"{file} does not exists")
except PermissionError:
    print(f"You don't have permission to delete {file}")
    
