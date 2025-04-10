def divisible (num):
    for i in range (num):
        divisble_number = i + 1
        if (  num % divisble_number == 0 ):
            print(divisble_number)
        

def main ():
    num = int( input("Enter a number : ") )
    divisible(num)

if __name__ == '__main__':
    main()