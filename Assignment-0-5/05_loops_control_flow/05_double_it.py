def main ():
    
    user_inp = int(input("Please enter a number: "))
    
    while (user_inp < 100 ):   
        user_inp = user_inp * 2
        print (user_inp, end=", ")
       

if __name__ == "__main__":
    main()


