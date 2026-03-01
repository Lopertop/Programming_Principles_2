import re

text = input()
pattern = r"([a-z])([A-Z])"
res = re.sub(pattern, r"\1_\2", text)

print(res.lower())
