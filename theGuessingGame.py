
#import random
from random import choice

#generating a random number within a range of values
#guessNum = random.randint(2, 7)
guessNum = choice(range(2,7))
#initialising the number of guesses made 
guessCount = 0
#initialisng the number of available guesses
guessLimit = 3

#condition for program to run
while guessCount < guessLimit:
    #failsafe incase user inputs ch, str or symbol instead of num
    try:
        guess = int(input("Guess the number between 2 and 6: "))
        if guess != guessNum:
            #reducing the number of chances left
            guessLimit -= 1
            print(f"Incorrect, you have {guessLimit} attempts left!")

        else:
            print("Correct, You Won!")
            break

    except ValueError:
        print("Invalid, input only a number between 2 to 7")
