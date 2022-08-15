import random
from words import words
import string


def getWord(words, mode):
    word = random.choice(words)
    l = 1 + mode * 2
    while '-' in word or ' ' in word or len(word) < l:
        word = random.choice(words)
    return word


def hangman():

    print(f"\nWelcome to Hangman Game, choosing difficulty and start the game.\n")
    mode = -1
    while mode < 0 or mode > 3:
        mode = int(input("\
 1.Easy         \n\
 2.Medium       \n\
 3.Hard         \n\n\
Your choice: "))
    # print(mode)
    if mode == 1:
        print(f"Easy Mode\n")
        lives = 10
    elif mode == 2:
        print(f"Medium Mode\n")
        lives = 6
    elif mode == 3:
        print(f"Hard Mode\n")
        lives = 3
    else: 
        print(f"Hardcore\n")
        mode = 4
        lives = 2

    word = getWord(words, mode).upper()
    word_set = set(word)
    print(word)
    guess = ''
    letters = set(string.ascii_uppercase)
    print(letters)
    attempt = set()
    while lives > 0 and len(word_set) > 0:
        print(f"You have {lives} lives, and you tried these letters:", ' '.join(attempt))

        word_list = [l if l in attempt else '-' for l in word]

        print(f"Current word: ", ' '.join(word_list))
        print(" ")
        
        guess = input("Make a guess: ").upper()
        
        if guess in letters - attempt:
            attempt.add(guess)
            if guess in word_set:
                word_set.remove(guess)
            else:
                lives -= 1
        elif guess in attempt:
            print(f"\nYou have already try {guess}. Try again.\n")
        else:
            print(f"\nInvalid input. Try again.\n")
    if lives > 0:
        print(f"\n You made it! The answer is ", word.lower())
    else:
        print(f"\n Fail! The answer is ", word.lower())
hangman()