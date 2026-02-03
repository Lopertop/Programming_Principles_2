# Basic Decorator
def changecase(func):
    def inner():
        return func().upper()
    return inner

@changecase
def my_function():
    return "Hello Sally"

@changecase
def otherfunction():
    return "I am speed!"

print(my_function())
print(otherfunction())

print("-------------")

# Arguments in the Decorated Function
def changecase2(func):
    def inner(x):
        return func(x).upper()
    return inner

@changecase2
def my_function2(name):
    return "Hello " + name

print(my_function2("John"))

print("-------------")

def changecase3(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return inner

@changecase3
def my_function3(name):
    return "Hello " + name

print(my_function3("Tobias"))

print("-------------")

#Decorator with Arguments
def changecase4(n):
    def changecase5(func):
        def inner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return inner
    return changecase5

@changecase4(1)
def my_function4():
    return "Hello Linus"

print(my_function4())

print("-------------")

# Multiple Decorators
def changecase6(func):
    def inner():
        return func().upper()
    return inner

def addgreeting(func):
    def inner():
        return "Hello " + func() + " Have a good day!"
    return inner

@changecase6
@addgreeting
def my_function5():
    return "Tobias"

print(my_function5())

print("-------------")

# Preserving Function Metadata
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)

print()

@changecase
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)

print()

import functools

def changecase7(func):
    @functools.wraps(func)
    def inner():
        return func().upper()
    return inner

@changecase7
def myfunction1():
    return "Have a great day!"

print(myfunction1.__name__)