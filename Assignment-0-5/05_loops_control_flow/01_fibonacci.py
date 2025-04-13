
MAX_NUMBER = 10000

def main():
    curr_num = 0
    next_num = 1

    while curr_num <= MAX_NUMBER:
        print (curr_num)
        next_term_num = curr_num + next_num
        curr_num = next_num
        next_num = next_term_num
        # print(next_term_num)


if __name__ == '__main__':
    main()

