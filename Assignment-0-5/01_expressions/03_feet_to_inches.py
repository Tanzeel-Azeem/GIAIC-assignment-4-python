def main():
    print("This program converts feet to inches.")
    
    user_feet_input = float(input("Enter feets: "))
    inches = user_feet_input * 12
    print(f"{user_feet_input} feet is equal to {inches:.2f} inches. \n")


if __name__ == '__main__':
    main()