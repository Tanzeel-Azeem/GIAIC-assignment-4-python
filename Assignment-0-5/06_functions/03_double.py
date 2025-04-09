def double (num):
    return num * 2

def main ():
    num = int( input ("\nEnter a number to give its double value: ") )
    num_times_two = double(num)
    print(f"The Double of your number is: {num_times_two}")


if __name__ == '__main__':
    main()