import random

score1 = {}
score2 = {}

play_again = ("yes")
while(play_again == "yes"):
    
    score1 = {}
    score2 = {}
    
    number = random.randint(1,6)
    print("What is your name?")
    name1 = input("> ")
    print("|ROLLED|")
    print(number)
    score1[number] = "first roll"
    print("Player one's score ", score1)

    print("next player")

    number = random.randint(1,6)
    print("What is your name?")
    name2 = input("> ")
    print("|ROLLED|")
    print(number)
    score2[number]="first roll"
    print("Player two's score ", score2)


    print("Round 2")


    number = random.randint(1,6)
    print("Player 1 - ", name1)
    input("Hit enter to roll")
    print("|ROLLED|")
    print(number)
    score1[number]="second roll"
    print("Player one's score ", score1)

    print("next player")

    number = random.randint(1,6)
    print("Player 2 - ", name2)
    input("Hit enter to roll")
    print("|ROLLED|")
    print(number)
    score2[number]="second roll"
    print("Player two's score ", score2)


    print("Round 3")


    number = random.randint(1,6)
    print("Player 1 - ", name1)
    input("Hit enter to roll")
    print("|ROLLED|")
    print(number)
    score1[number]="third roll"
    print("Player one's score ", score1)

    print("next player")

    number = random.randint(1,6)
    print("Player 2 - ", name2)
    input("Hit enter to roll")
    print("|ROLLED|")
    print(number)
    score2[number]="third roll"
    print("Player two's score ", score2)



    print("-------------")

    print(name1, score1)
    print(name2, score2)


    if(score1 > score2):
        print("Player 1 wins!")
    elif(score1 < score2):
        print("Player 2 wins!")
    else:
        print("TIE!!")

    play_again = ()
    play_again = input("play again? yes or no > ")
