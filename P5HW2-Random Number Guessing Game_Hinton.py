#Random Guessing Game, the computer picks a random number between 1 and 100.
#It will tell you if the guess is too high, too low or correct.

#July 8, 2018
#CTI-110 P5HW2-Random Number Guesisng Game
#Debbie Hinton

import random

def generateSecretNumber():
    secretNumber = random.randint( 1, 100)
    return secretNumber

def askUserForNumber( message = 'Guess the number:'):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber( userNumber, secretNumber):
    if userNumber > secretNumber:
        return 'Too high'
    elif userNumber < secretNumber:
        return 'Too low'
    else:
        return 'Congratulations!'

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        secretNumber = generateSecretNumber()
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, secretNumber )

        while message != 'Congratulations!':
            print(message)
            userNumber = askUserForNumber( 'Try again:')
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber( userNumber, secretNumber )

            print()
            print( message, "And it took you", userNumberOfGuesses,\
                   "tries")
            print()
            userCongratulated = True

main()

        
    
