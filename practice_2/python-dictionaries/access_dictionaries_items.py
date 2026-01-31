thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x)

y = thisdict.get("model")
print(y)

print("--------------")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

print("--------------")

x = car.values()
print(x)

car["year"] = 2020
print(x)

print("--------------")

x = car.items()
print(x)

car["color"] = "red"
print(x)

print("--------------")

if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")