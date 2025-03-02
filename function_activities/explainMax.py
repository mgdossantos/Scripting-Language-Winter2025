d = {'a': 10, 'b': 20, 'c': 30}

max_key = max(d, key=d.get)
print(max_key)  # Output: 'c'