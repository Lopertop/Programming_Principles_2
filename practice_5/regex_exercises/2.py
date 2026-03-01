import re

text = input()
pattern = r"ab{2,3}"
match = re.search(pattern, text)

if match:
    print(match.group())
else:
    print("No match")
