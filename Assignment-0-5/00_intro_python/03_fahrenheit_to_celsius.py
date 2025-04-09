
def main ():
    print("This program will convert temperature from Fahrenheit to Celsius")
    degrees_fahrenheit = float(input("Enter the value you want to convert into celcius:  "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"{degrees_fahrenheit} degrees Fahrenheit is equal to {degrees_celsius} degrees Celsius")

if __name__ == "__main__":
    main()
