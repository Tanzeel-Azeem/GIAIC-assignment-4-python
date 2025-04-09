def first_letter (lst):
    print(lst[0])
def get_first_letter():
    lst = []
    msg =  input("Please enter an element of the list or press enter to stop. ")

    while msg != '':
        lst.append(msg)
        msg = input("Please enter an element of the list or press enter to stop. ")
        return lst
def main():
    lst = get_first_letter()
    first_letter(lst)

if __name__ == '__main__':
    main()