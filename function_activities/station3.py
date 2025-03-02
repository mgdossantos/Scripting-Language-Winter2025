def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def reverse_list(lst):
    return lst[::-1]

def reverse_list_in_place(lst):
    lst.reverse()

def remove_duplicates_keep_order(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Testing the functions
print(find_average([34, 36, 38, 40, 40]))
print(find_average([]))  # Output: 0

original_list = [34, 36, 38, 40, 40]
print(reverse_list(original_list))
print(original_list)

reverse_list_in_place(original_list)
print(original_list)

print(remove_duplicates_keep_order([34, 36, 38, 40, 40]))