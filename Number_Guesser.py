#Michael Stroup
#Number Guersser
#11/11

#Init
import random

#Functions
def number_guess():
#Difficulty, changes numbers based on selected setting
    print("Welcome to the Secret Number Guesser. Pick a difficulty.")
    level = input("easy/medium/hard")
    print("input a number to begin.")
    #User input/guess
    if level == "easy":
        NumGuess = int(input("Enter Number: Zero through five. You have 3 lives"))
        y = random.randint(0,5)
    elif level == "medium":
        NumGuess = int(input("Enter Number: Zero through Ten. You have 3 lives"))
        y = random.randint(0,10)
    elif level == "hard":
        NumGuess = int(input("Enter Number: Zero through twenty. You have 3 lives"))
        y = random.randint(0,20)
    else:
        print("Wrong input. Please enter easy/medium/hard to select difficulty.")
        number_guess()
#Number picker/ correct / Play again?
    if NumGuess == y:
        print(str(NumGuess) + " Is Correct")
        print("Would you like to play again?")
        z = input("yes or no")
        if z == "yes":
            number_guess()
        elif z == "no":
            print("Have a nice day!")
            return
    #if number answer was wrong, two guesses left
    else:
        print(str(NumGuess) + " Is wrong. Try again. You have 2 lives")
        NumGuess = input("Enter a new number.")
        if NumGuess == y:
            print(str(NumGuess) + " Is Correct")
            print("Would you like to play again?")
            z = input("yes or no")
            if z == "yes":
                number_guess()
            elif z == "no":
                print("Have a nice day!")
                return
    #If guess was wrong, one guess left
        else:
            print(str(NumGuess) + " Is wrong. Try again. You have 1 lives")
            NumGuess = input("Enter a new number.")
            if NumGuess == y:
                print(str(NumGuess) + " Is Correct")
                print("Would you like to play again?")
                z = input("yes or no")
                if z == "yes":
                    number_guess()
                elif z == "no":
                    print("Have a nice day!")
                    return
    #if wrong, tell the number and ask to play again
            else:
                print(str(NumGuess) + " Is Wrong. The Number was " + str(y) + ("."))
                print("Would you like to play again?")
                z = input("yes or no")
                if z == "yes":
                    number_guess()
                elif z == "no":
                    print("Have a nice day!")
                    return

#Main
number_guess()
