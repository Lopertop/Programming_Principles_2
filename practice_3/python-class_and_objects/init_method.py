class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)

print("-------------")

class Human:
    pass

p2 = Human()
p2.name = "Tobias"
p2.age = 25

print(p2.name)
print(p2.age)

print("-------------")

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p3 = Person("Emil")
p4 = Person("Tobias", 25)
print(p3.name, p3.age)
print(p4.name, p4.age)

print("-------------")

class Info:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
    
info1 = Info("Emil", 30, "Oslo", "Norway")
print(info1.name)
print(info1.age)
print(info1.city)
print(info1.country)