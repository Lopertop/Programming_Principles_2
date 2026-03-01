import re

text = input()
pattern = r"[A-Z][^A-Z]*"
res = re.findall(pattern, text)

print(res)