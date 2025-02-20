### Creating a List
my_list = [1, 2, 3, 4, 5]
empty_list = []
mixed_list = [1, "hello", 3.14, [10, 20]]

print("Initial Value")
for item in my_list:
    print(item)

# ### Adding Elements to a List
my_list.append(10)  # Adds to the end
print("after append")

for item in my_list:
    print(item)

my_list.insert(2, 99)  # Inserts at index 2
print("after insert")
for item in my_list:
    print(item)
#
#
# ### Removing Elements from a List
my_list.remove(3)  # Removes first occurrence of 3
print("after remove")
for item in my_list:
    print(item)

deleted = my_list.pop(2)  # Removes element at index 2
print("deleted element:" + str(deleted))

print("after pop")
for item in my_list:
    print(item)
# #
# ### Accessing Elements
first_element = my_list[0]
last_element = my_list[-1]
print("Some elements in the list ")
print(first_element)
print(last_element)
# #
# ### Slicing Lists
sub_list = my_list[1:4]  # Elements from index 1 to 3

print("sub list")
for item in sub_list:
    print(item)

# ### Sorting and Reversing Lists
my_list.sort()  # Sorts in ascending order
my_list.reverse()  # Reverses the list
#
# # ### Common List Methods
length = len(my_list)  # Gets length of the list
count = my_list.count(2)  # Counts occurrences of 2
index = my_list.index(4)  # Finds the index of 4
