#Write a Python program that asks the user
#for their name and age, writes this information
#to a file called user_info.txt, and then
#reads the file to display its contents.

def user():
    name= input("Type your name: ")
    age = input ("Type your age:")
    return name,age

def writeFile(info):
    with open("user_info.txt", "w") as f:
        f.write(info[0]+ "--" + info[1])

def printFile():
    with open("user_info.txt", "r") as f:
        print(f.read())