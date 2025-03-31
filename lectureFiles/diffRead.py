with open("sample.txt", "a") as f:
    f.write("\nat College Lasalle ")

print("\n ** Using read ***")
with open("sample.txt", "r") as file:
    content = file.read()  # Reads the whole file
    print(content)

print("\n ** Using readline ***")
with open("sample.txt", "r") as file:
    first_line = file.readline()  # Reads the first line
    second_line = file.readline()  # Reads the next line
    print(first_line)
    print(second_line)
print("\n ** Using readline2 ***")
with open("sample.txt", "r") as file:
    line = file.readline()
    while line:
        print(line)
        line= file.readline()
#
print("\n ** Using readlines ***")
with open("sample.txt", "r") as file:
    lines = file.readlines()  # Reads all lines and stores them in a list
    print(lines)

print("\n ** Using strip ***")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # Removes extra newline characters