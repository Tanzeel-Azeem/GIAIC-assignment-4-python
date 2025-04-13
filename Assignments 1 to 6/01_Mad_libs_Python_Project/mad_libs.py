def main():
    print("\nWelcome to the Tiny Mad Libs!")
    
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    
    print("\nHere's your Tiny Mad Libs story:")
    print(f"Once upon a time, there was a {adjective} {noun} who loved to {verb}.\n")

if __name__ == '__main__':
    main()