import random

choice=['rock', 'paper', 'scissors']

def user_choice():
    while True:
        userChoice=str(input("Choose rock, paper or scissors : ")).lower()
        if userChoice in choice:
            return userChoice
        else:
            print("Invalid choice! Please enter rock, paper or scissors.")

def py_choice():
    return random.choice(choice)

def winner(userChoice, pyChoice):
    if userChoice==pyChoice :
        print("It's a tie!")
    elif (userChoice=="rock" and pyChoice=="scissors") or \
         (userChoice=="paper" and pyChoice=="rock") or \
         (userChoice=="scissors" and pyChoice=="paper"):
        print ("You won!")
    else :
        print("You lose!")

def main():
    start=str(input("Wanna play a game? (yes/no): ")).lower()
    if start=="yes":
        while True :
            userChoice = user_choice()
            pyChoice = py_choice()
            print("You have chosen ", userChoice)
            print("Python has chosen ", pyChoice)
            winner(userChoice, pyChoice)
            
            again=str(input("Want a rematch? (yes/no): ")).lower()
            if again != "yes":
                print("Thanks for playing. See you next time!")
                break

main()
