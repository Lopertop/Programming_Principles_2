def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

print("-------------")

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

print("---------------")

def large_sequence(n):
    for i in range(n):
        yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

print("---------------")
list_comp = [x * x for x in range(5)]
print(list_comp)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

print("---------------")
total = sum(x * x for x in range(10))
print(total)

print("---------------")
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(100):
    print(next(gen))

print("---------------")

def echo_generator():
    while True:
        received = yield
        print("Received:", received)
    
gen = echo_generator()
next(gen)
gen.send("Hello")
gen.send("World")

print("---------------")
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()