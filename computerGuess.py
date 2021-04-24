import random
from time import sleep

def computerGuess(number_range):
    feedback = "" # feedback the user gives (c, h or l)
    low = 1
    high = number_range
    feedback = ""

    while feedback != "C":
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low

        print("Computer guessing number ...\n")
        sleep(1)
        feedback = input(f"Is {computer_guess} too High (H), too Low (L) or is it correct (C)?: ").upper()

        if feedback == "H":
            high = computer_guess -1
        elif feedback == "L":
            low = computer_guess + 1

    print(f"\nComputer guessed the number {computer_guess} correctly")

def userInput():
    number_range = int(input("Definde a range in which the number is contained: "))

    computerGuess(number_range)

userInput()
    

# user input number that computer has to guess and also the range in which this number is contained
# computer guesses number randomly
# user gets three options to choose from (either c = correct, h = too high or l = too low)
# computer changes random guessing range based on user input and guesses again
# loop until number is guessed correctly