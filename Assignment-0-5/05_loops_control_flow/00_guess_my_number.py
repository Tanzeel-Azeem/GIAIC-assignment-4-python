import random

def main():
    print("\n welcomem to guess the number game ")

    random_num = random.randint(1, 99)
    user_guess = int(input("guess a number between 1 and 99: "))

    while (user_guess != random_num):
        if (user_guess> random_num):
            print("guess lower")
        else:
            print("guess higher")
        
        user_guess = int(input("\nguess again : "))

    print(f"you guessed it! the number was {random_num}")


if __name__ == "__main__":
    main()