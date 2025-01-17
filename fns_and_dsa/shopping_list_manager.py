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
            item = input('what item do you want to add to your shopping list? ')
            shopping_list.append(item)
            print(f'Added {item} to your shopping list. ')
  
        elif choice == '2':
            item = input('Which item do you want to remove from your shopping list? ')
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'Removed {item} from your shoppig list. ')
            else:
                print('{item} is not found in your shoppig list')
       
        elif choice == '3':
            print(shopping_list)
       
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()