#file = open("sample.txt", "w")
with open("sample.txt", "w") as f:
    f.write("Marcela Dos Santos")

with open("sample.txt", "a") as f:
    f.write("\nBest Python Teacher!! ")

print("** Using Read ***")
with open("sample.txt", "r") as f:
    print(f.read())

#
