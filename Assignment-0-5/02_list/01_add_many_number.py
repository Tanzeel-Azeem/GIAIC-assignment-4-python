def add_numbers (num):

    total = 0
    for number in num:
        total += number
    return total


def main ():
    num : list [int] = [1, 2, 3, 4, 5]
    result = add_numbers(num)
    print(f'The sum of the numbers is: {result}')
  
if __name__ == '__main__':
    main()