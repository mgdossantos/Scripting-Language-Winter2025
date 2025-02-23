import csv

with open("../../lecture12/students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("../../lecture12/students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 20, "A"])