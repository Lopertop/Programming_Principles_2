fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print("-----------")

for x in fruits:
    if x == "banana":
        break
    print(x)