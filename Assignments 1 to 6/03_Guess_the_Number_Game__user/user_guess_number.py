import random

def user_guess ():
    random_number = random.randint(1, 10)
    user_guess = int(input ("Guess a number between 1 - 10: "))

    while user_guess != random_number:
      

        if (user_guess > random_number):
            print("Your guess is high")
        elif (user_guess < random_number):
            print("Your guess is low")

        user_guess = int(input ("Guess again number between 1 - 10: "))    


    print("You guessed it correctly")



user_guess()            