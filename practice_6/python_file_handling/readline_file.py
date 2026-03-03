with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

print("--------------------------------")

with open("demofile.txt") as f:
    for x in f:
        print(x)