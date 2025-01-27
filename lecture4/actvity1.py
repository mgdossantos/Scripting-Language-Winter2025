import random
# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
print(secret_number)
number = int(input("Type a number: "))
count=1
while number !=secret_number:
    if number < secret_number:
        print("Trya again with a big number!!")
    else:
        print("Trya again with a lower number!!")

    number = int(input("Type a number: "))


print("Congratulations!!!")


