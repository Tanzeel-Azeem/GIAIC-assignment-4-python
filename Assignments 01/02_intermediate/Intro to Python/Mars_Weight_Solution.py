MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.08
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0



def main():
    user_weight = int(input ("Enter you weight in kg: "))
    user_planet = input("Enter a planet: ")

    if (user_planet == 'Mercury'):
        weight_on_mercury = user_weight * MERCURY_GRAVITY
        print(weight_on_mercury)

    elif (user_planet == "Venus"):
        weight_on_venus = user_weight * VENUS_GRAVITY
        print(weight_on_venus)
        
    elif (user_planet == "Mars"):
        weight_on_mars = user_weight * MARS_GRAVITY
        print(weight_on_mars)

    elif (user_planet == "Jupiter"):
        weight_on_jupiter = user_weight * JUPITER_GRAVITY
        print(weight_on_jupiter)

    elif (user_planet == "Saturn"):
        weight_on_saturn = user_weight * SATURN_GRAVITY
        print(weight_on_saturn)

    elif (user_planet == "Uranus"):
        weight_on_uranus = user_weight * URANUS_GRAVITY
        print(weight_on_uranus)
    elif (user_planet == "Neptune"):
        weight_on_neptune = user_weight * NEPTUNE_GRAVITY
        print(weight_on_neptune)
    else:
        print("Please write a valid planet or try capital letter")
   



if __name__ == '__main__':
     main()