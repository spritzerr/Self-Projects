print("Helloo!!")
while True :
    question=str(input("Will you come to prom with me? Yes or no. "))
    question=question.lower()

    if question=="yes" :
        print("Yay! I'll be sure to pick u up. See ya!")
        break
        
    elif question=="no" :
        print("So mean :<")
        break
        
    else :
        print("Can't even give a straight answer?")
