#Write a program to receive number and give
# the cumulative sum  for the odd (%)
# number and the cumulative sum for the
# even number. Use 0 to stop your program.
odd_num=0
even_num = 0
number = -1
while number !=0:

    number =  int(input("Enter Numbers: "))

    if number != 0:
        if number % 2 ==0 :
            even_num+= number
        else :
            odd_num+= number

print(f"Sum of Even is :" + str(even_num))
print(f"Sum of odd is :" + str(odd_num))









