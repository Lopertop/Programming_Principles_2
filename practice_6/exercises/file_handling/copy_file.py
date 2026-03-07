from shutil import copy2
import os

source = "sample.txt"
destination = "experimental_folder"

if not os.path.exists(destination):
    os.mkdirs(destination)

try:
    copy2(source, destination)
    print(f"File '{source}' has been copied to '{destination}' successfully.")
except Exception as e:
    print(f"An error occurred: {e}")