def print_multiple(message, repeats):
    return (message + '!' + ' ')  * repeats


def main ():
    message = input("Enter a message: ")
    repeats = int(input("Enter how many times to repeat the message: "))
    value = print_multiple(message, repeats)
    print(value)


if __name__ == "__main__":
    main()