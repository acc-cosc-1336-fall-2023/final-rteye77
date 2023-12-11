#add import
import question_d

def main():
    while True:
        
        multiplication_table = question_d.create_multiplication_table()
        question_d.display_multiplication_table(multiplication_table)

        choice = input("Do you want to continue (y/n)? ")
        if choice.lower() != 'y':
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()