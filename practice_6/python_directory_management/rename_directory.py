import os

os.rename("my_directory", "renamed_directory") # Single rename
os.renames("old_dir", "new_parent/new_child/renamed_directory") # Rename and create missing parent directories if needed
