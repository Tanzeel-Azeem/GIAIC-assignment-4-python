def add_three_words (my_list, data):
    for i in range (3):
        my_list.append(data)

def main ():
    data = input("Please enter a word: ")
    my_list = []
    print(f"my list before: {my_list}")
    add_three_words(my_list, data)
    print(f"my list after: {my_list}")

if __name__ == '__main__':
    main()