import json

# Initial data
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data2.json", "w") as file:
    json.dump([data], file, indent=4)  # Store as a list

#Read and append new data
with open("data2.json", "r") as file:
    existing_data = json.load(file)  # Load existing JSON as a list
    #print(existing_data)
#
# New data to append
new_entry = {"name": "Marcela", "age": 41, "city": "Montreal"}
existing_data.append(new_entry)  # Append new data

# Write updated data back to the file
with open("data2.json", "w") as file:
    json.dump(existing_data, file, indent=4)  # Overwrite with updated list

# Verify by reading
with open("data2.json", "r") as file:
    final_data = json.load(file)
    for element in final_data:
        print(element)