
# MAX_NUMBER = 10000

# def main():
#     curr_num = 0
#     next_num = 1

#     while curr_num <= MAX_NUMBER:
#         print (curr_num)
#         next_term_num = curr_num + next_num
#         curr_num = next_num
#         next_num = next_term_num
#         # print(next_term_num)


# if __name__ == '__main__':
#     main()

MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()