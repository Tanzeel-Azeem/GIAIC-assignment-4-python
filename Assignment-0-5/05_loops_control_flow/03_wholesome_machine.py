def main ():
    print ("Welcome to the Wholesome Machine!")

    wholesome_message = "I am capable of doing anything I put my mind to"
    user_inp = input(f"\nPlease write this line correcty =  {wholesome_message} : \n")
    
    while (user_inp != wholesome_message):
        if ( user_inp == wholesome_message):
            print ("You did it!")
        else:
            print ("You failed!")
            user_inp = input(f"Please write this line correcty:  {wholesome_message} \n")

    print ("You did it!")

if __name__ == "__main__":      
    main()