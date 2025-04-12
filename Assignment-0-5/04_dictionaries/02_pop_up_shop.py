def main():
    total_amount = 0

    fruits_in_shops = {
        'apple' : 2,
        'banana': 5,
        'mangoes': 12,
        'grapes': 5,
        'melon': 3
    }

    for fruits in fruits_in_shops:
        price = (fruits_in_shops[fruits])
        user_purcahase = int( input(f"How many {fruits} you want to buy?  "))

        total_amount += (price * user_purcahase)
    
    print(f"Your total is ${total_amount}")


if __name__ == '__main__':
    main()