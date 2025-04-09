
def main():
    lst = []
    value = input("Please enter an element of the list or press enter to stop. ")
    
    while value:
        lst.append(value)
        value = input("Please enter an element of the list or press enter to stop. ")
    
    print(lst)


if __name__ == '__main__':
    main()