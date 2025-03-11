import json

data = {"name": "Alice", "age": 25, "city": "New York"}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

#Parameters:
#data: The Python dictionary or list to be written as JSON.
#file: The file object where JSON data will be saved.
#indent=4: Makes the JSON human-readable by formatting it with
# 4 spaces per indentation level.

with open("data.json", "r") as file:
    data = json.load(file)
    print(data["name"])
