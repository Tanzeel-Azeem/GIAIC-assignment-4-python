JOKE = "Feminism"
PROMPT = "What do you want? "
SORRY = 'Sorry I only tell jokes'

def main() :
    user_inp = input(PROMPT)

    if 'joke' in user_inp:
        print(JOKE)
    else:
        print(SORRY)


if __name__ == '__main__':
    main()

