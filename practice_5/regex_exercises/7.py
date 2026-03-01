import re

text = input()
pattern = r"_([a-zA-Z0-9])"
res = re.sub(pattern, lambda m: m.group(1).upper(), text)

print(res)