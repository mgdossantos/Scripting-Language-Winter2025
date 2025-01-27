while True:
    name = input("Enter name (more than 3 characters): ")
    if len(name) <= 3:
        print("Error: Name must be greater than 3 characters.")
        continue

    try:
        age = int(input("Enter age (between 0 and 150): "))
        if age < 0 or age > 150:
            print("Error: Age must be between 0 and 150.")
            continue
    except ValueError:
        print("Error: Age must be a number.")
        continue

    try:
        salary = float(input("Enter salary (greater than 0): "))
        if salary <= 0:
            print("Error: Salary must be greater than 0.")
            continue
    except ValueError:
        print("Error: Salary must be a numeric value.")
        continue

    gender = input("Enter gender ('f' or 'm'): ").lower()
    if gender not in ['f', 'm']:
        print("Error: Gender must be 'f' or 'm'.")
        continue

    marital_status = input("Enter marital status ('s', 'c', 'v', 'd'): ").lower()
    if marital_status not in ['s', 'c', 'v', 'd']:
        print("Error: Marital status must be 's', 'c', 'v', or 'd'.")
        continue

    print("All information is valid.")
    break