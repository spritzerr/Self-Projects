print("Finding Area of Triangle or Rectangle")
print("Please make your selection :")

while True : #Looping choice
    print("********************")
    print("* 1. Triangle        *")
    print("* 2. Rectangle     *")
    print("* 3. End               *")
    print("********************")

    choice = float(input("Pick your option : ", ))

#Calculating Area of Triangle
    if choice == 1 :
        widthT = float(input("Enter width of triangle : ", ))
        height = float(input("Enter height of triangle : ", ))
        areaT = (1/2)*widthT*height
        print("Area of Triangle : ", areaT)

#Calculating Area of Rectangle
    elif choice == 2 :
        length = float(input("Enter length of rectangle : ", ))
        widthR = float(input("Enter width of rectangle : ", ))
        areaR = length*widthR
        print("Area of Rectangle : ", areaR)

#Ends the program
    elif choice == 3 :
        print("Thank you for using this program!")
        break

#Invalid choice
    else :
        print("Invalid choice, please pick again.")
