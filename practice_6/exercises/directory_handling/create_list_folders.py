import os

nested_folders = "experimental/data/foldar_last"
os.makedirs(nested_folders, exist_ok=True)

for dirpath, dirnames, filenames in os.walk("experimental"):
    print(f"Current path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"files: {filenames}")
