def last_letter (lst):
    print(lst[-1])


def get_last_letter():
    lst = []
    msg =  input("Please enter an element of the list or press enter to stop. ")

    while msg != '':
        lst.append(msg)
        msg = input("Please enter an element of the list or press enter to stop. ")
        return lst
def main():
    lst = get_last_letter()
    last_letter(lst)

if __name__ == '__main__':
    main()