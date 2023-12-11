#add import
import question_a


def main():
    stocks = question_a.get_stock_list()
    if not stocks:
        return

    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nStock List:")
            question_a.display_stock_list(stocks)
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()