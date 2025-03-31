import csv
print("*** Creating csv file ***")
with open("students3.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])

with open("students3.csv", "w", newline='') as file:
    writer = csv.writer(file)
    for i in range(3):
        name = input("Type your name: ")
        age = int(input("Type your age: "))
        grade = input("Type your age: ")
        writer.writerow([name,age,grade])


print("*** Printing csv file ***")
with open("students2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)