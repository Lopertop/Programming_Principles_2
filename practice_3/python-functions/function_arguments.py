def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("-------------")

def my_function1(name): # name is a parameter
    print("Hello,", name)

my_function1("Emil") # Emil is an argument

print("-------------")

def my_function2(fname, lname): # Function expexts 2 arguments
    print(fname + " " + lname)

my_function2("Emil", "Refsnes") # And gets 2 agruments

print("-------------")

# Default Parameter Values
def my_function3(name = "friend"):
    print("Hello", name)

my_function3("Emil")
my_function3()
my_function3("Tobias")
my_function3("Linus")

print("-------------")

# Keyword Arguments
def my_function4(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function4(animal = "dog", name = "Buddy")
my_function4(name = "Buddy", animal = "dog")

print("-------------")

# Positional Arguments
my_function4("dog", "Buddy")
my_function4("Buddy", "dog")

print("-------------")

# Mixing Positional and Keyword Arguments
def my_function5(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function5("dog", name = "Buddy", age = 5)

print("-------------")

# Passing Different Data Types
def my_function6(fruits):
    for fruit in fruits:
        print(fruit)
    
my_fruits = ["apple", "banana", "cherry"]
my_function6(my_fruits)

print()

def my_function7(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function7(my_person)

print("-------------")

# Return Values
def my_function8(x, y):
    return x + y

result = my_function8(5, 3)
print(result)

print()

def my_function9():
    return ["apple", "banana", "cherry"]

fruits = my_function9()
print(fruits[0], fruits[1], fruits[2])

print()

def my_function10():
    return (10, 20)

x, y = my_function10()
print("x:", x)
print("y:", y)

print("-------------")

# Positional-Only Arguments
def my_function11(name, /):
    print("Hello", name)

my_function11("Emil")

print("-------------")

# Keyword-Only Arguments
def my_function12(*, name):
    print("Hello", name)

my_function12(name = "Emil")

print("-------------")

# Combining Positional-Only and Keyword-Only
def my_function13(a, b, /, *, c, d):
    return a + b + c + d

result = my_function13(5, 10, c = 15, d = 20)
print(result)