#add import
import question_c

def main():
    while True:
        dna_string1 = input("Enter a DNA string (length > 8 and <= 16): ")
        if question_c.check_dna_string(dna_string1):
            break
        else:
            print("Invalid length. DNA string should be greater than 8 and less than or equal to 16 characters.")

    while True:
        dna_string2 = input("Enter a DNA substring (length = 4): ")
        if question_c.check_substring(dna_string2):
            break
        else:
            print("Invalid length. DNA substring should be exactly 4 characters.")

    positions = question_c.get_most_likely_ancestor_consensus(dna_string1, dna_string2)
    print("Number of DNA substring in the DNA string:", end=" ")
    for pos in positions:
        print(pos, end=" ")
    print()


if __name__ == "__main__":
    main()