import random

while True :
    print()
    print("Shall we start?")
    print("1. Yes")
    print("2. No")
    print()
    
    start = int(input("It's your choice : "))
    
    if start==1 :
        
        number = random.randint(1, 6)
        print(number)
        print()
        action = int(input("Pick a number from 1 to 6 : "))

        if action < 1 or action > 6:
            print("The number you picked is not valid. Try again.")

        else :
            if action == number :
                print("BANG! You Died.")
                print()
                print("1. Yes")
                print("2. No")
                start = int(input("Play again? : "))
                if start!=1 :
                    print("See you next time.")
                    break
                
            else :
                print("Phew, You Live.")
    
    else :
        print("See you next time.")
        break


