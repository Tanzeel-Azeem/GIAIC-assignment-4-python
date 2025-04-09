def main():
    print("This program calculates the energy equivalent of mass using Einstein's famous equation E=mc^2.")
    
    m = float(input("Enter mass in kilograms: "))
    c = 299792458
    e = m * c**2


    print("\nApplying Einstein's equation E=mc^2")
    print(f"m =  {m} kg")
    print(f"c = {c} m/s")
    print(f"The energy equivalent of {m} kg is {e:.2f} joules. \n")

if __name__ == '__main__':
    main()