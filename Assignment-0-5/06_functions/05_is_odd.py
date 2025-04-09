def is_odd (value):
    reminder = value % 2
    return reminder == 1


def main():
    for i in range (10):
        if is_odd(i):
            print("odd")
        else:
            print('even')

if __name__ == '__main__':
    main()