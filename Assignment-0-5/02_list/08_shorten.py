MAX_LENGTH = 5


def shorten (lst):
    while len(lst) > MAX_LENGTH:
        last_element_pop = lst.pop()
        print( last_element_pop )

def get_last ():
    lst = []
    msg = input("please enter a word or press enter to stop. ")
    
    while msg != '':
        lst.append(msg)
        msg = input("please enter a word or press enter to stop. ")
        return lst
    
def main ():
    lst = get_last()
    shorten (lst)
  

if __name__ == '__main__':
    main()       