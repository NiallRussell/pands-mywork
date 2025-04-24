#Guess the word from a defined list of words

import random

name = input("What is your name?")

print(f'Good Luck {name}!')

words = ["microcreds", "GPS", "student", "learner", "course director", "meeting", "international", "ECCTIS", "NOOSR", "Allegro", "Scholars", "Stables", "traffic", "coffee", "Teams", 
         "lotto", "Academic Registry", "reception", "HEA", "ERB", "education", "application", "Radius"]

word = random.choice(words)

length = len(word)
print(f"The word has {length} characters")

print("Guess the characters")

guesses = ""
turns = 12

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        elif char == " ":
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("\nYou win!")
        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guess_upper = guess.upper()
    
    guesses += guess
    guesses += guess_upper

    if guess not in word and guess_upper not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses")
    else:
        print ("Correct")

        if turns == 0:
            print("You lose :(")