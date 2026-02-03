# Arbitary Arguments - *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function2(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function2("Emil", "Tobias", "Linus")

print("----------------")

# Using *args with Regular Arguments
def my_function3(greeting, *names):
    for name in names:
        print(greeting, name)

my_function3("Hello", "Emil", "Tobias", "Linus")

print("----------------")

# Sum of any number of values
def total_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(total_sum(1, 2, 3))
print(total_sum(10, 20, 30, 40))
print(total_sum(5))

print("----------------")

# Find maximum value from number of values
def max_value(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(max_value(3, 7, 2, 9, 1))

print("----------------")

# Arbitary Keyword Arguments - **kwargs
def my_function4(**kid):
    print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")

def my_function5(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function5(name = "Tobias", age = 30, city = "Bergen")

print("----------------")

# Using **kwargs with Regular Arguments
def my_funtion6(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_funtion6("emil123", age = 25, city = "Oslo", hobby = "coding")

print("----------------")

# Combining *args and **kwargs
def my_function7(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function7("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

print("----------------")

# Unpacking Arguments
def my_function8(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function8(*numbers)
print(result)

def my_function9(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function9(**person)