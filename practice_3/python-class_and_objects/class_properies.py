class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

print("--------------")

p2 = Person("Tobias", 25)
print(p2.age)

p2.age = 26
print(p2.age)

print("--------------")

p3 = Person("Linus", 30)

del p3.age

print(p3.name)
# print(p3.age) # This will cause an error

print("--------------")

class Person:
    species = "Human" # class property

    def __init__(self, name):
        self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

print("--------------")

class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

print("--------------")

class Person:
    def __init__(self, name):
        self.name = name
    
p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)