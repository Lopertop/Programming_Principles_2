import re

# The findall() function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x = re.findall("Portugal", txt)
print(x)

print("------------------")

# The search() function
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("Portugal", txt)
print(x)

print("-------------------")

# The split() function
x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

print("------------------")

# The sub() function
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)
