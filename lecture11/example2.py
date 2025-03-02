# Using curly braces
student = {
    "name": "Marcela",
    "age": 23,
    "major": "Computer Engineer"
}

# Using dict() function
employee = dict(name="Alice", position="Manager", salary=60000)

# Accessing Dictionary Elements

print(student["name"])  # Output: Marcela
print(employee["salary"])  # Output: 60000
print(student)
# # Adding a new key-value pair
student["GPA"] = 3.8

print(student)
#
#
# # Updating an existing key-value pair
student["age"] = 26
print(student)
#
# #print(student)  # Output: {'name': 'Marcela', 'age': 26, 'major': 'Computer Engineer', 'GPA': 3.8}
#
# Removing Elements

del student["major"]  # Removes 'major' key
print(student)  # Output: {'name': 'Marcela', 'age': 26, 'GPA': 3.8}

# Using pop()
ageV = student.pop("age")
print(ageV)  # Output: 26
print(student)