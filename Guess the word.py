#Hangman
while True:
    print()
    print("Welcome to Spritzer's Wordle!")
    print("You have 5 hints before you are able to submit an answer.")
    print()
    
    print("Start?")
    print("1. Yes")
    print("2. No")
    start=int(input("Choose 1 or 2 : "))
    
    if start==1 :
        for i in range(5) :
            print("_ _ _ _ _")
            guess=str(input("Put in your guess : ")).lower()
            correct=["a", "p", "l", "e"]
            
            if len(guess) == 1 :
                if guess in correct :
                    print("That letter is present somewhere in the word!", i + 1)
                    print()
                
                else :
                    print("That letter is not present in the word.", i + 1)
                    print()
            
            else :
                print("Please input only 1 letter to continue.", i + 0)
            
        print("You have ran out of hints. ")
        answer=str(input("Submit your guess here : ")).lower()
        
        
        if answer.lower()=="apple" :
            print("Your answer is correct!")
        else :
            print("You are wrong.")
            print("Please try again.")
    
    else :
        print("Thank You!")
        break
        
    
    