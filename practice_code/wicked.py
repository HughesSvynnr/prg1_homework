print("please enter 5 numbers with spaces")
numbers = input("> ")
split = numbers.split(" ")
if(len(numbers)==5):
    sum = 0
    for sx in numbers:
        x = float(sx)
        sum +=x
        
    print(sum," is not your final score")

    score = 0
    for swicked in numbers:
        wicked=float(swicked)
        if(wicked == 13.0):
            score += -100
        elif(wicked == 7.0):
            score += 30
        elif(wicked %2 == 1):
            score += wicked * 2
        elif(wicked %2 == 0):
            score += wicked/2
        else:
            print("Not valid")
    print(score, " is your final score :)")
else:
    print("U did not enter numbers correctly you no know counting. :(")