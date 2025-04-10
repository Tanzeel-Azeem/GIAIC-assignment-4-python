
def in_stock (fruit):
    if fruit == 'apple':
        return 200
    if fruit == 'banana':
        return 150
    if fruit == 'mango':
        return 100
    else:
        return 0

def main():
    fruit = input("\nEnter a fruit you want to buy: ")
    stock = in_stock(fruit)
    
    if (stock == 0):
        print(f"Sorry {fruit}  is not available")
    else:
        print(f"{fruit}  is available, we have {stock} {fruit} at the moment\n")
        

if __name__ == '__main__':
    main()