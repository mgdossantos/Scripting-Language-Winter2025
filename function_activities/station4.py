import modulestation4 as st4

# Testing the functions
print(st4.min_max(([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])))  # Output: (1, 9)
print(st4.min_max([]))  # Output: (None, None)

print(st4.min_max_sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: (1, 9)
print(st4.min_max_sorted([]))  # Output: (None, None)

print(st4.swap_first_last((1, 2, 3, 4, 5)))  # Output: (5, 2, 3, 4, 1)
print(st4.swap_first_last(()))  # Output: ()

print(st4.tupxle_to_sorted_list((3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(st4.tuple_to_sorted_list(()))  # Output: []