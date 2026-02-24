import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

x= re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())