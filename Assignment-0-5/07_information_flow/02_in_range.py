low = 5
high = 100


def in_range (n, low, high):
    if (n > low and n < high):
        return True
    return False

def main():
    n = int(input("Enter a number to see if it's in range : "))
    print( in_range(n, low, high) )



if __name__ == '__main__':
    main()