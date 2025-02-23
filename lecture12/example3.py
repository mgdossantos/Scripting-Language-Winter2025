file = open("../../lecture12/sample.txt", "w")
file.write("Hello, Python!")
file.close()

with open("../../lecture12/sample.txt", "r") as file:
    print(file.read())  # Reads the whole

with open("../../lecture12/sample.txt", "w") as file:
    file.write("This will replace the existing content.\n")


with open("../../lecture12/sample.txt", "a") as file:
    file.write("This is a new line added.\n")