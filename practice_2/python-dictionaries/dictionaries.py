thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964, 
   # "year": 2020 - Cannot have duplicates
    "colors": ["red", "white", "blue"]
}

print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

print("--------")

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)