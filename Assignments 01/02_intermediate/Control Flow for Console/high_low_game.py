import random

NUM_ROUNDS = 5

def main():
    user_score = 0
   
    
    print("Welcome to the High low game!")
    print("-------------------------------")
    
    for i in range (NUM_ROUNDS):
        print(f"\nRound -", i + 1)

        user_number = random.randint(1,99)
        computer_number = random.randint(1,99)
        print(f"Your Number is {user_number}")


        user_guess = str(input("Do you think your number is higher or lower than the computer's?: "))


        while user_guess!= 'higher' and user_guess!= 'lower':
            user_guess = str(input("Do you think your number is higher or lower than the computer's?: "))

        higher_and_Correct = (user_number > computer_number)
        lower_and_correct =  (user_number < computer_number)
        
        if (higher_and_Correct) or (lower_and_correct):
            user_score += 1
            print (f"That's correct wonderful... Computer guess was : {computer_number}")
            print (f"Your score : {user_score}")

        else:
            print(f"Aww thats wrong ... Computer guess was : {computer_number}")

   
    print("\nYour total score is : ", user_score)
    
    if (user_score == 5):
        print("\nWow! You played perfectly!")
    elif (user_score == 4) or (user_score == 3):
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")



if __name__ == '__main__':
    main()