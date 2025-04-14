import random
from words import words
import string

def get_valid_word (words):

    random_word = random.choice(words)

    return random_word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set(  )
    live = 6

    while len( word_letters ) > 0 and live > 0:
        
        print(f"You have {live} live left \nYou have used these charecter: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add( user_input )
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                live -=1
                print("Letter is not in word")
        
        elif user_input in used_letters:
            print("You have already used that charecter. Try different one")
        
        else:
            print("Invalid Charecter")

    if live == 0:
        print("You lost the word is: ", word)
    else:
        print(f"Letss goo you've guessed the word: {word}")
   
hangman()