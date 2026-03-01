import re

text = input()
pattern = r"[\s,.]"
res = re.sub(pattern, ":", text)

print(res)
