from ALGORITHM_1_LFCO_2025_JR_LR_DA import generate, print_strings
from ALGORITHM_2_LFCO_2025_JR_LR_DA import print_results
from ALGORITHM_3_LFCO_2025_JR_LR_DA import print_configurations_table



def menu():
    strings = []
    while True:
        print("\n=== PDA MENU ===")
        print("1. Generate strings")
        print("2. Input strings")
        print("3. Validate strings in the PDA")
        print("4. Print tree for the strings accepted by the PDA")
        print("5. Clear string list")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            strings = generate()
            print_strings(strings)
        elif choice == "2":
            str = input("Enter strings separated by commas: ").split(',')
            for s in str:
                strings.append(s)
            print("New List:")
            print_strings(strings)
        elif choice == "3":
            if strings:
                print_results(strings)
            else:
                print("No strings to validate.")
        elif choice == "4":
            if strings:
                for s in strings:
                    print_configurations_table(s)
            else:
                print("No strings to print.")

        elif choice == "5":
            strings = []
            print("String list cleared.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
menu()
