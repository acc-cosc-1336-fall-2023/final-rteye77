#add import
import question_b

def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            question_b.stock_purchase_history()
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()