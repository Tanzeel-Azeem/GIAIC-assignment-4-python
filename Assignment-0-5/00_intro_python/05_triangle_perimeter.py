def main():
   print("This program will calculate the perimeter of a triangle")

   side1 : float = float(input("enter the length of side 1 of triangle: "))
   side2 : float = float(input("enter the length of side 2 of triangle: "))
   side3 : float = float(input("enter the length of side 3 of triangle: "))

   perimeter :float = side1 + side2 + side3
   print(f"\nThe perimeter of the triangle is: {perimeter}")

   
if __name__ == '__main__':
    main()