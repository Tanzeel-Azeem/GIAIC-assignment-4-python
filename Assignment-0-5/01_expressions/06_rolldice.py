import random

def main():
    print("\nWelcome to the Dice Simulator!")

    max_dice_count = 6

    dice1 = random.randint(1, max_dice_count)
    dice2 = random.randint(1, max_dice_count)
    total = dice1 + dice2
    print(f"\nFirst dice rolled: {dice1}")
    print(f"Second dice rolled: {dice2}")
    print(f"The total of two dice is : {total}\n")

if __name__ == '__main__':
    main()
