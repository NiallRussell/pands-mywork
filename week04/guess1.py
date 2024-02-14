import random
number = random.randint(0,100)
guess = int(input("Guess the number:"))
while guess != number:
    if guess < number:
        print("Too low")
        guess = int(input("Please guess again: "))
    else: 
        print("Too high")
        guess = int(input("Please guess again: "))

print (f"Well done! The number was {number}")