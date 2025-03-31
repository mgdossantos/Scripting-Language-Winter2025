import csv
print("*** Creating csv file ***")
with open("students2.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["Alice", 20, "A"])
    writer.writerow(["Marcela", 41, "B"])
print("*** Printing csv file ***")
with open("students2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
