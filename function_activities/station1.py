# Write a function greet(name) that takes a name
# as input and returns "Hello, [name]!".
# Write a function square(number) that
# returns the square of a number.
# Test your functions by calling them with different values.
# Bonus Challenge:
# Modify greet(name) to include an optional greeting message.
# If no message is provided, default to "Hello".
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# def greet (name):
#     return ("Hello, "+name)

def square(number):
    return number ** 2

# Testing the functions
print(greet("Marcela"))
print(greet("Priscila", "Ola"))
print(square(4))
print(square(9))