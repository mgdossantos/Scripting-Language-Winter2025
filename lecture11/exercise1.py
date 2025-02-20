# Program to read four values, store them in a tuple, and analyze the values

number1 = int(input("Enter the first value: "))
number2 = int(input("Enter the first value: "))
number3 = int(input("Enter the first value: "))
number4 = int(input("Enter the first value: "))
values = (number1, number2,number3,number4)

print(values)

count_nines = values.count(9)
print("The value 9 appeared {} times.".format(count_nines))

print(str(values.index(3)))

even_number=[]
for items in values:
    if items %2 ==0:
        even_number.append(items)


print(even_number)
