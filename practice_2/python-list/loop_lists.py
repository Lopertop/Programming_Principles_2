thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

print("-----")

for i in range(len(thislist)):
    print(thislist[i])

print("-----")

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

print("-----")

[print(x) for x in thislist]