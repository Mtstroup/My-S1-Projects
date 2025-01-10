#Michael Stroup
#1/6/25
#Rock Paper Scissors
#Init
import random
wins = 0
losses = 0
ties = 0
#Functions
def game():
    #Intro
    global wins
    global losses
    global ties
    print("Welcome to Rock Paper Scissors.")
    print("Select rock/paper/scissors to start")
    while True:
        #user input
        player = input("Type selection:")
        #Computer random selection and transfer to variable
        computer = random.randint(1,3)
        if computer == 1:
            computer = "rock"
            print("computer selected rock")
        if computer == 2:
            computer = "paper"
            print("computer selected paper")
        if computer == 3:
            computer = "scissors"
            print("computer selected scissors")

        #Outcome
        if player == computer:
            print("You tied.")
            ties = ties + 1
        elif player == "rock" and computer == "paper":
            print("You lose.")
            losses = losses + 1
        elif player == "rock" and computer == "scissors":
            print("You win.")
            wins = wins + 1
        elif player == "paper" and computer == "rock":
            print("You win.")
            wins = wins + 1
        elif player == "paper" and computer == "scissors":
            print("You lose.")
            losses = losses + 1
        elif player == "scissors" and computer == "rock":
            print("You lose.")
            losses = losses + 1
        elif player == "scissors" and computer == "paper":
            print("You win.")
            wins = wins + 1
        #Stats and Play again
        print("Stats")
        print("Wins: " + str(wins))
        print("Losses: " + str(losses))
        print("Ties: " + str(ties))
        print("would you like to play again?")
        play_again = input("yes/no:")
        if play_again == "no":
            print("Thanks for playing.")
            break
        else:
            print("Restarting")

#Main
game()
