def main():
    print("\nThis program calculates the remainder of a division.")
    
    value1 = int(input("Enter the first integer to be divided : "))
    value2 = int(input("Enter the second integer to be divided : "))

    division_value = value1 // value2
    remainder_value = value1 % value2

    print(f"The result of this division is {division_value} with a remainder of {remainder_value}.\n")
if __name__ == '__main__':
    main()