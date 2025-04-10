ADULT_AGE : int = 18

def person_age (age: int):
    if (age >= ADULT_AGE):
        return True
    return False


def main ():
    age = int(input("How old are you? "))
    
    print(person_age(age))

if __name__ == '__main__':
    main()