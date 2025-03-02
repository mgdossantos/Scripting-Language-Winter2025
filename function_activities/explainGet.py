# Example dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Using get to retrieve existing keys
name = person.get('name')  # Output: 'Alice'
age = person.get('age')    # Output: 25

# Using get to retrieve a non-existing key with a default value
country = person.get('country', 'Unknown')  # Output: 'Unknown'

# Using get to retrieve a non-existing key without a default value
zip_code = person.get('zip_code')  # Output: None

print(name)     # Output: Alice
print(age)      # Output: 25
print(country)  # Output: Unknown
print(zip_code) # Output: None