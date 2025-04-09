def main ():

    user_height = int(input("Enter your height in inches: "))
    minimum_height_limit = 50

    if (user_height >= minimum_height_limit):
        print("You are tall enough to ride the roller coaster.")
    else:
        print("You are not tall enough to ride the roller coaster.")

if __name__ == '__main__':
    main()