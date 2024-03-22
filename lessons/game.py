"""Number Guessing Game."""
from random import randint    

SECRET: int = randint(1,10)
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        # something to help us exit
        correct = True
    else:
        print("Guess again!")