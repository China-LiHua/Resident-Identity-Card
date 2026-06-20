import datetime

def main():
    # Initialization
    error_List = []
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    id_number = input("Please enter an 18-digit Chinese Resident Identity Card number: ")

    # Length verification
    if len(id_number) != 18:
        error_List.append("Length is not equal to 18 digits")

    # Character verification
    if len(id_number) == 18:
        try:
            if id_number[17] in ("X", "x"):
                int(id_number[:17:1])
            else:
                int(id_number)
        except ValueError:
            error_List.append("Contains non-digit characters")

    # Date verification
    if len(id_number) == 18:
        try:
            birth_date = datetime.datetime.strptime(id_number[6:14:1], "%Y%m%d")
            if birth_date > datetime.datetime.now():
                Error_List.append("Invalid date of birth")
        except ValueError:
            error_List.append("Invalid date of birth")

    # Checksum verification
    if len(id_number) == 18:
        total_sum = 0
        for x in range(17):
            total_sum += factors[x] * int(id_number[x])
    
        if check_codes[total_sum % 11] != id_number[17].upper():
            error_List.append("Checksum verification failed")

    # Output results
    print("-" * 30)
    if len(error_List) > 0:
        print("Invalid ID card format, details:")
        for error in error_List:
            print(f"  ·{error}")
    else:
        print("Hint: The ID card format is completely valid!")

        # Output information
        print()
        print("ID Card Information:")
        if int(id_number[16]) % 2 == 0:
            print("Gender: Female")
        else:
            print("Gender: Male")
        print(f"Date of Birth: {birth_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
