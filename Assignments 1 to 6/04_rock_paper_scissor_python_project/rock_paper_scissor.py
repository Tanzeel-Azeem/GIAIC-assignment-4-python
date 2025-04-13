import random

CHOICES = ["rock", "paper", "scissor"]

def play ():

    print("\n=======WELCOME TO ROCK PAPER SCISSOR GAME================")
    computer_choice = random.choice(CHOICES)
    user_choice = input("Enter your choice: ")


    if (user_choice == computer_choice):
        result = f"##### It's a tie! You choose {user_choice} and computer choose {computer_choice}"
        print(result)
        # print("It's a tie")

    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = f"##### You Win! You choose {user_choice} and computer choose {computer_choice}"
        print(result)
    else:
        result = f"##### You Loose! You choose {user_choice} and computer choose {computer_choice}"
        print(result)
        

play()