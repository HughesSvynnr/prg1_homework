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