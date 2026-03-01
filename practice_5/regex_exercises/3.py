import re

text = input()
pattern = r"([a-z]+_[a-z]+)"
matches = re.findall(pattern, text)

if matches:
    print(", ".join(matches))
else:
    print("No matches")
