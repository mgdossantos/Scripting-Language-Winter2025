# Creating a tuple with different data types
person = ("Marcela", 41, "Engineer", "Brazil")

# Using the tuple() function
#person = tuple(["Marcela", 41, "Engineer"])


# Accessing elements by index
print(person[1])  # Output: 41

# Slicing a tuple
print(person[1:3])  # Output: (41, 'Engineer')

#Tuple Unpacking

name, age, profession,country = person
print(name)       # Output: Marcela
print(age)        # Output: 41
print(profession) # Output: Engineer

person[0] = "Benicio"  # This will raise a TypeError