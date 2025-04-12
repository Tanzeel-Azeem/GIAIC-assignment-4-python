import random

def main ():
    random_num = random.randint(1, 99)
    print("i'm thinking of a number from 1 to 99!")
    user_guess = int(input("Enter a number: "))

    while (user_guess != random_num):
        if (user_guess > random_num):
            print("your guess is high")
        else:
            print("your guess is low")
        
        print()

        user_guess = int(input("Enter a number: "))

    print("You guessed it")




if __name__ == '__main__':
    main()