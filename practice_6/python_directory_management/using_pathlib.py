from pathlib import Path

Path("my_new_dir").mkdir(exist_ok=True)

for file in Path(".").iterdir():
    print(file)