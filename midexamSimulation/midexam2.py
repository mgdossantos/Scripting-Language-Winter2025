
shopping_list = []
while True:
    print("\nSmart Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View all items")
    print("4. Check item")
    print("5. Exit")
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
