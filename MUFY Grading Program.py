#Looping the program
while True:
    
    #Input grade
    grade = int(input("Enter your grade : "))
    
    #Switch case for grades at different ranges
    if grade>100 :
        print("Invalid grade enter again.")
        
    elif grade>=80 :
        print("Your grade is High Distinction, HD.")

    elif grade>=70 :
        print("Your grade is Distinction, D.")
        
    elif grade>=60 :
        print("Your grade is Credit, C.")

    elif grade>=50 :
        print("Your grade is Pass, P.")
        
    elif grade<50 :
        print("Your grade is Fail, N.")

        
