#Michael Stroup
#10/17
#Name Generator
#Init

#Functions
def question():
    #welcome
    print("Welcome to Brawl Stars main picker!")
    print("Answer the questions with yes or no to find out your main.")
#Questions
    ans = input("Do you play Brawl Stars: yes or no")
    if ans == "yes":
        ans = input("Do you trickshot in Brawl Stars: yes or no")
        if ans == "yes":
            ans = input("Do you spin in Brawl Stars: yes or no")
            #Outcome
            if ans == "yes":
                print("You are a Edgar main")

            elif ans == "no":
                print("You are a Colt main")

        elif ans == "no":
            ans = input("Do you use the X spray: yes or no")
            #Outcome
            if ans == "yes":
                print("You are a Surge main")

            elif ans == "no":
                print("You are a Stu main")

    elif ans == "no":
        ans = input("Would you consider playing Brawl Stars: yes or no")
        if ans == "yes":
            ans = input("Would you spend money on the game: yes or no")
            #outcome
            if ans == "yes":
                print("You are a Gale main")

            elif ans == "no":
                print("You are a Piper main")

        elif ans == "no":
            ans = input("If your friends wanted you to play, would you: yes or no")
            #outcome
            if ans == "yes":
                print("You are a Spike main")

            elif ans == "no":
                print("You are a Poco main")

#bad input message
        else:
            print("Plese anser with yes or no. Try again.")


#main
question()
