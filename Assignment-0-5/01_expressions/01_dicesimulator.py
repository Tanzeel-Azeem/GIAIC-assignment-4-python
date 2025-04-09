import random

def dice():
    max_dice_count = 6

    dice1 = random.randint(1, max_dice_count)
    dice2 = random.randint(1, max_dice_count)
    total = dice1 + dice2
    # print(f"\nFirst dice rolled: {dice1}")
    # print(f"Second dice rolled: {dice2}")
    print(f"The total of two dice is : {total}")

def main ():
    print ("Welcome to the Dice Simulator!")
    dice()
    dice()
    dice()
    

if __name__ == '__main__':
    main()