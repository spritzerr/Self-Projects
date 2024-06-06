import random
import math

choice=['rock', 'paper', 'scissors']
totalWin=0
totalTie=0

def py_choice1():
    return random.choice(choice)

def py_choice2():
    return random.choice(choice)

def winner(pyChoice1, pyChoice2):
    global totalWin
    global totalTie
    if pyChoice1==pyChoice2 :
        print("It's a tie!")
        print()
        totalTie += 1
        
    elif (pyChoice1=="rock" and pyChoice2=="scissors") or \
         (pyChoice1=="paper" and pyChoice2=="rock") or \
         (pyChoice1=="scissors" and pyChoice2=="paper"):
        print ("Python1 won!")
        print()
        totalWin += 1
        
    else :
        print("Python1 lose!")
        print()

def main():
    print("[Simulation Start]")
    while True :
        rep=int(input("How many times would you like to run the simulation?: "))
        if rep<1 :
            print("[Simulation End]")
            break
        else :
            i=0
            while i<rep:
                pyChoice1 = py_choice1()
                pyChoice2 = py_choice2()
                print("Python1 has chosen ", pyChoice1)
                print("Python2 has chosen ", pyChoice2)
                winner(pyChoice1, pyChoice2)
                i+=1
            
            prob=totalWin/rep
            percent="{:.2f}".format(prob*100)
            expected=rep*prob
            var=rep*prob*(1-prob)
            sd=math.sqrt(var)
            
            print("For Python1 : ")
            print("Total Repetitions :", rep)
            print("Total wins :", totalWin)
            print("Total losses :", rep - totalWin - totalTie)
            print("Total ties :", totalTie)
            print("Probability of winning :", prob)
            print("Percentage :", percent, "%")
            print("Expected value :", expected)
            print("Variance :", var)
            print("Standard Deviation: ", sd)
            print()

main()


