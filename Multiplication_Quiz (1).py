#Michael Stroup
#1/8
#Multiplication Quiz
#Init
import random
#Functions
def game():
    score = 0
    question = 1
    #Welcome
    print("Welcome to the Multiplication Quiz.")
    while True:
        #length of quiz
        print("How long would you ike the quiz?")
        length = int(input("Number of questions:"))
        #Difficulty
        print("Select a difficulty for the quiz: easy, medium, or hard")
        difficulty = input("Enter: easy/medium/hard")
        print("Please enter an answer for the quiz to begin.")
        #Questions
        for i in range(length):
            if difficulty == "easy":
                num1 = random.randint(1,5)
                num2 = random.randint(1,5)
            elif difficulty == "medium":
                num1 = random.randint(1,10)
                num2 = random.randint(1,10)
            elif difficulty == "hard":
                num1 = random.randint(10,20)
                num2 = random.randint(10,20)
            print("Question " + str(question) + " out of " + str(length))
            print("What is " + str(num1) + " x " + str(num2))
            #User answer
            ans = int(input("Answer:"))
            if ans == num1 * num2:
                print(str(ans) + " Is Correct!")
                score = score + 1
            elif ans != num1 * num2:
                print(str(ans) + " Is Wrong")
            question = question + 1
        #Final score
        print("Quiz complete. Your final score is:")
        print(str(score) + " out of " + str(length))
        print("would you like to play again?")
        play_again = input("Enter: yes/no")
        if play_again == "yes":
            print("restarting")
        elif play_again == "no":
            print("Thanks for playing.")
            break
#Main
game()
