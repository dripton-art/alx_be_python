# Shopping List Manager.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter an item to add: ") # Prompt for and add an item
            shopping_list.append(item)
            print(f"{item} has been added to the list!")
            print()
            pass
        elif choice == '2':
            item = input("Enter an item to remove: ") # Prompt for and remove an item
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list!")
                print()
            else:
                print(f"{item} not found!")
                print()
            pass
        elif choice == '3':
            print("Your shopping list:", shopping_list) # Display the shopping list
            print()
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()