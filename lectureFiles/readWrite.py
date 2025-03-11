with open("sample.txt", "w") as file:
    file.write("Marcela dos Santos. ")

print("** Using Read ***")
with open("sample.txt", "r") as file:
    print(file.read())

with open("sample.txt", "a") as file:
    file.write("\nBest Python Teacher!! ")

print("\n ** Using a to add a line ***")
with open("sample.txt", "r") as file:
    print(file.read())
