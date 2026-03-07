from functools import reduce

a = ["Geeks", "for", "Geeks"]
r = reduce(lambda x, y: x + " " + y, a)
print(r)

b = [5, 9, 3, 12, 7]
r1 = reduce(lambda x, y: x if x > y else y, b)
print(r1)