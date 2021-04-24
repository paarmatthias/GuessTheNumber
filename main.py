import random
import datetime


#test

def guess(defRange):
    random_number = random.randint(1, defRange)
    guess = 0

    guesses = 0 # number of guesses the user made
    guessRange = defRange/3 # number of guesses the user can take
    time = str(datetime.datetime.now()) # get the current time

    while guess != random_number:
        if guesses < guessRange:
            guess = int(input(f"Guess a number between 1 and {defRange}: "))
            if guess > random_number:
                print("Guess is to High, guess again!")
            elif guess < random_number:
                print("Guess is to Low, guess again!")
            else:
                print("You guessed correctly!")
                ScoreSheet = open("/Users/paarmatthias/Documents/Programming/Python/GuessTheNumber/ScoreSheet.txt", "a")
                ScoreSheet.write("Win! " + time + "\n")
            guesses += 1
        else:
            print("\nYou took too many guesses!")
            print("Good luck next time!")
            ScoreSheet = open("/Users/paarmatthias/Documents/Programming/Python/GuessTheNumber/ScoreSheet.txt", "a")
            ScoreSheet.write("Loss! " + time + "\n")
            break

def defineRange():
    defRange = int(input("Define a guessing Range: "))
    print("\n")
    return defRange

defRange = defineRange()
guess(defRange)
