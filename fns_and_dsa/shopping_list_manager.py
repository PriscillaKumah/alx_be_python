def display_menu()
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    # Start with an empty list
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Add item
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f" '{item}' has been added to your shopping list.")
            else:
                print(" You must enter an item name.")

        # Remove item
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}' has been removed from your shopping list.")
            else:
                print(f"❌ '{item}' not found in the shopping list.")

        # View list
        elif choice == '3':
            if shopping_list:
                print("\n Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print(" Your shopping list is empty.")

        # Exit program
        elif choice == '4':
            print(" Goodbye! Thanks for using Shopping List Manager.")
            break

        # Invalid option
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")


# Run the program only if this script is executed directly
if __name__ == "__main__":
    main()

