def display_menu():
    print("\nSmart Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View all items")
    print("4. Check item")
    print("5. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_items(shopping_list):
    if shopping_list:
        print("\nShopping List:")
        index = 1
        for item in shopping_list:
            print(f"{index}. {item}")
            index += 1
    else:
        print("The shopping list is empty.")

def check_item(shopping_list):
    item = input("Enter the item to check: ")
    if item in shopping_list:
        print(f"'{item}' is in the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")


shopping_list = []
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_item(shopping_list)
    elif choice == "2":
        remove_item(shopping_list)
    elif choice == "3":
        view_items(shopping_list)
    elif choice == "4":
        check_item(shopping_list)
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
