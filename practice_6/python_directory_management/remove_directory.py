import os

dir_path = "k:/files"

if not os.listdir(dir_path):
    os.rmdir(dir_path)
    print("Directory removed successfully")
else:
    print("Error! Directory not empty")

# shutil.rmtree(path) # Removes a directory and all its contents
