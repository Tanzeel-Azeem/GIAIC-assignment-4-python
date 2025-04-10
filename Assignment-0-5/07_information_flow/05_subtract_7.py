def subtract_seven (num):
    num = num - 7
    return num

def main():
    num = int( input("enter a number to get subtracted by 7: ") )
    num = subtract_seven(num)
    print(num)


if __name__ == "__main__":
    main()