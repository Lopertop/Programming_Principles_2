from pathlib import Path

directory = Path("experimental")
text_files = list(directory.rglob("*.txt"))

print(text_files)