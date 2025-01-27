while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if password == username:
        print("Error: Password cannot be the same as the username. Please try again.")
    else:
        print("Username and password accepted.")
        break