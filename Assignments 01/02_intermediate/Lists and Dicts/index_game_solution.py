def access_element( lst, index ):
    try:
        return lst[index]
    except IndexError:
        return "Invalid index Number"
    
def modify_element (lst, index, new_value):
    try:
         lst[index] = new_value
         return lst
    except IndexError:
        return "Invalid index Number"
    
def slice_element(lst, start, end):
    return lst [start: end]


def index_game():
    lst = [1, 2, 3, 4, 5 ]

    print(f"Current List: {lst}")
    print("Choose an Operation: access, modify, slice")
    user_operation = input("Write an Operation: ")


    if (user_operation == 'access'):
        index = int(input("Enter index to access: "))
        print (access_element(lst, index))

    elif (user_operation == 'modify'):
        index = int( input("Enter index to Modify: ") )
        new_value = input("Enter a new value: ")
        print (modify_element(lst, index, new_value))
    
    elif (user_operation == 'slice'):
        start = int(input("Enter a starting index: "))
        end = int(input("Enter a ending index: "))
        print (slice_element(lst, start, end))

    else:
        print("Invalid operation.")

index_game()