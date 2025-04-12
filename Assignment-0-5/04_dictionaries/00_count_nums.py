def get_user_num ():

    user_numbers = []

    while True:
        user_input = input("Enter a Number: ")

        if user_input == '':
            break
        
        num = int(user_input)
        user_numbers.append(num)

    return user_numbers


def is_present (num_lst):

    num_dictionary = {}

    for num in num_lst:
        if (num not in num_dictionary):
            num_dictionary[num] = 1
        else:
            num_dictionary[num] += 1
            
    return num_dictionary


def counts_of_numbers (num_dictionary):
    for num in num_dictionary:
        print(f"{num} appears {num_dictionary[num]}  times")


def main ():
    user_numbers =  get_user_num()
    num_dictionary = is_present(user_numbers)
    counts_of_numbers (num_dictionary)


if __name__ == '__main__':
    main()