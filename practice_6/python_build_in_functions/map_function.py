def myfunc(n):
    return len(n)

x = map(myfunc, ("apple", "banana", "cherry"))
for i in x:
    print(i)

def myfunc_1(a, b):
    return a + b

x = map(myfunc_1, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineaapple'))

for i in x:
    print(i)