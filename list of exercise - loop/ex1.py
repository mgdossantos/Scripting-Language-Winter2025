#Program to ask for a grade between zero and ten.
# Show a message if the value is invalid and keep
# prompting until the user enters a valid value

while True:
    try:
        grade = float(input("Enter a grade between 0 and 10: "))
        if 0 <= grade <= 10:
            print(f"Valid grade: {grade}")
            break
        else:
            print("Invalid grade, please enter a value between 0 and 10.")
    except ValueError:
        print("Invalid input, please enter a numeric value.")