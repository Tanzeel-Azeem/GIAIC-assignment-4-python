import random

def computer_guess():
    low = 1
    high = 10
    ans = ''
    print("\nThink of a number under 10 and the computer has to guesss it !")

    
    while ans != 'c':
        guessing_number = random.randint(low, high)
        ans = input(f"Is {guessing_number} is high (h) or low (l) or Correct (c): ")

        if (ans == 'h'):
            high = guessing_number -1
        elif (ans == 'l'):
            low = guessing_number + 1


    print("\nThe Computer has guessed it correctly\n")

computer_guess()