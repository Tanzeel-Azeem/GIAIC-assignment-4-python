def user_name_number ():
    phonebook = {}

    while True:
        name = input("Name: ")
        if (name == ''):
            break
        number = int(input("Number: "))

        phonebook[name] = number

    return phonebook



def print_names( phonebook ):

    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")




def lookup_numbers (phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == '':
            break
        if name not in phonebook:
            print("this person is not in phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = user_name_number()
    print_names(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()