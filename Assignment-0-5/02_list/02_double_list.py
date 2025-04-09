def main ():
    
    numbers : list [int] = [1, 2, 3, 4, ]

    for i in range( len ( numbers ) ):
        number_at_index = numbers[i] 
        numbers[i] = number_at_index * 2
        
    print ( f'The double of the numbers is: {numbers}' )

if __name__ == '__main__':
    main()