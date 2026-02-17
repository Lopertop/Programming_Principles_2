# Local Scope
def myfunc():
    x = 300
    print(x)

myfunc()

print("------------")

# Function Inside Function
def myfunc1():
    x = 300
    def myinnerfunc1():
        print(x)
    myinnerfunc1()

myfunc()

print("------------")

# Global Scope
x = 300

def myfunc3():
    print(x)

myfunc3()
print(x)

print("------------")

# Naming Variables
x = 300

def myfunc4():
    x = 200
    print(x)

myfunc4()
print(x)

print("------------")

# Global Keyword
def myfunc5():
    global y
    y = 300

myfunc5()
print(y)

print()

z = 300

def myfunc6():
    global z
    z = 200

myfunc6()
print(z)

print("------------")

# Nonlocal Keyword
def myfunc7():
    name = "Jane"
    def myfunc8():
        nonlocal name
        name = "hello"
    myfunc8()
    return name

print(myfunc7())

print("------------")

# The LEGB Rule (1. Local, 2. Enclosing, 3. Global, 4. Built-in)
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)