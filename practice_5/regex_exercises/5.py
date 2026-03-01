import re

text = input()
pattern = r"a\w+b\b"
match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No match")
