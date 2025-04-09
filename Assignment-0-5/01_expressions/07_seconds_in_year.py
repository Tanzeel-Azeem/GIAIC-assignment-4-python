def main():
    print("\nThis program calculates the number of seconds in a year.")
    user_year_input = int(input("Enter your Year: "))

    if (user_year_input == '1'):
        second_in_year = 60 * 60 * 24 * 365
        print(f"There are {second_in_year} seconds in a year.")
    else:
        second_in_year = 60 * 60 * 24 * (365 * user_year_input)
        print(f"There are {second_in_year} seconds in {user_year_input} years.\n")


if __name__ == '__main__':
    main()