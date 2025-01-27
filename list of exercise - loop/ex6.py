numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(f"The sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {average}")