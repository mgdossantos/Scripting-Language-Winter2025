# Initialize an empty dictionary
key_value_pairs = {}

# Loop to collect three key-value pairs from the user
for i in range(3):
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    key_value_pairs[key] = value

# Print each key and value in the dictionary
for key, value in key_value_pairs.items():
    print(f"{key}: {value}")


