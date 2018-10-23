print("How many times do you wish to count?")
number = int(input("> "))


y = 0
while(y < number):
    stars = ""
    x = 0
    while(x < number):
        stars += "*"
        x=x+1
    print(stars)
    y+=1

    
