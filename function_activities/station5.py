def count_occurrences(lst):
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

def key_with_highest_value(d):
    if not d:
        return None
    #The get method in Python is used with dictionaries to
    # retrieve the value associated with a given key.
    # If the key is not found in the dictionary,
    # it returns a default value instead of raising a KeyError.
    # This makes it a safe way to access dictionary values,
    # especially when the key might not be present.
    return max(d, key=d.get)

def sort_dict_by_values_desc(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

# Testing the functions
print(count_occurrences([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}

d = {'a': 10, 'b': 20, 'c': 30}
print(key_with_highest_value(d))  # Output: 'c'

print(sort_dict_by_values_desc(d))  # Output: {'c': 30, 'b': 20, 'a': 10}