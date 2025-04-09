import math

def main():
    print("Welcome to the Pythagorean Theorem Calculator!")

    AB = float(input("\nEnter the length of side AB: "))
    AC = float(input("Enter the length of side AC: "))

    BC :float = math.sqrt(AB**2 + AC**2)
    print(f"The length of side BC is: {BC:.2f}\n")

if __name__ == '__main__':
    main()