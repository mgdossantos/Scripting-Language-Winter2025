#file = open("sample.txt", "w")
#file.write("Hello, Python!")
#file.close()

with open("sample.txt", "w") as file:
    file.write("This is a new file. ")

with open("sample.txt", "w") as file:
    file.write("This line delete the content before. ")

with open("sample.txt", "a") as file:
    file.write("This is an additional text.")

with open("sample.txt", "a") as file:
    file.write("\nThis is an additional line.")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
        print("*")