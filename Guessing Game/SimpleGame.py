"""Implement the business logic of a simple logic game"""

import random

#Generate a random number for the user to guess
randNum = random.randrange(0,10)

#Let the user try to guess the number three time
for guessCounter in range(3):
    #Ask the user to guess the number
    #Input always gives us string
    userGuess = int(input('So what do you think is the number'))

    #printing the generated number and the user input
    print(f'The generated number is {randNum} and you guessed {userGuess}')

    #Check if he user guessed correctly
    if userGuess > randNum:
        print("Sorry, your guess is too high. Please try again")
    elif userGuess < randNum:
        print("Sorry, your guess is too low. Please try again")
    else:
        print("Congratulations. You have guessed correctly")
        break
else:
    print("Game over!")
    
