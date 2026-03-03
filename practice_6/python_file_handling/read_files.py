f = open("C:\\Users\\admin\\OneDrive\\Desktop\\python_cource\\practice_6\\python_file_handling\\demofile.txt")
print(f.read())
f.close()

print("------------------------------------------")

with open("demofile.txt") as f:
    print(f.read())

print("------------------------------------------")

with open("demofile.txt") as f:
    print(f.read(5))