import re

text = input()
pattern = r"[A-Z][a-z]+"
matches = re.findall(pattern, text)

if matches:
    print(", ".join(matches))
else:
    print("No matches")