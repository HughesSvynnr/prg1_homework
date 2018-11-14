def countup(count=0):
    if(count>10):
        return
    else:
        print(count)
        return countup(count + 1)
    pass

countup()

print("~~~~~~~~")

def countdown(count = 10):
    if(count<1):
        return
    else:
        print(count)
        return countdown(count - 1)

countdown()

print("~~~~~~~~~~~~~~~~")


def simple(bunnies):
    if(bunnies == 0):
        return 0
    else:
        return 2+simple(bunnies - 1)
print(simple(6))

print("~~~~~~~~~~")



def complex_bunnies(bunnies):
    if(bunnies == 0):
        return 0
    elif(bunnies %2 == 0):   #even bunnies
        return 2 + complex_bunnies(bunnies - 1)
    else:
        return 3 + complex_bunnies(bunnies - 1)

print(complex_bunnies(5))