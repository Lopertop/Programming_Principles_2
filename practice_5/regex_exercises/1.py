import re

text = input()
pattern = r"ab*"
match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No match")