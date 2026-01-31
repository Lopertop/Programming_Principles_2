# Unoin of Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

set3  = set1.union(set2)
print(set3)

set3_1 = set1 | set2
print(set3_1)

myset = set1.union(set2, set3, set4)
myset_1 = set1 | set2 | set3 | set4
print(myset)
print(myset_1)

print("------------")

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

setA = {"a", "b", "c"}
setB = {1, 2, 3}
setA.update(setB)
print(setA)

print("------------")

# Intersection of Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
set3_1 = set1 & set2
print(set3)
print(set3_1)

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

print("------------")

# Difference of Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"gooogle", "microsoft", "apple"}
set3 = set1.difference(set2)
set3_1 = set1 - set2
print(set3)
print(set3_1)

set1.difference_update(set2)
print(set1)

print("------------")

# Symmetric Difference of Sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
set3_1 = set1 ^ set2
print(set3)
print(set3_1)

set1.symmetric_difference_update(set2)
print(set1)