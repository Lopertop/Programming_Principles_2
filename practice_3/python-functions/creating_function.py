def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()

# Function Names:
# calculate_sum()
# _private_function()
# myFunction2()

# From Fahrenheit to Celcius
def fahreheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahreheit_to_celcius(77))
print(fahreheit_to_celcius(95))
print(fahreheit_to_celcius(50))

print("-----------")

# Return Values
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)
print(get_greeting())

# Pass Statement
def my_function():
    pass