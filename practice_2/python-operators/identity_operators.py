# is - Return True if both variables are the same object
# is not - Returns True if both variables are not the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
print("---------")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)