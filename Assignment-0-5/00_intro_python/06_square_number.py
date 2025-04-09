def main():
    print("This program will calculate the square of a number")
    user_num : int = int(input("Enter a number to find its square: "))
    square_num :int = user_num * user_num

    print(f"The square of {user_num} is: {square_num}")

if __name__ == '__main__':
    main()