'''
problem 1

Ask a user for a number. Depending on the number, respond with how many factors exist within that number

for example:
    Enter a number
>15
    15 has 4 factors, which are 1 3 5 15

'''


'''
problem 2
Write a program that will ask a user for a word. For that word, replace each letter with 
the appropriate letter of the phonetic alphabet.
For instance

    Enter a word
>balloon
Bravo Alpha Lima Lima Oscar Oscar November

'''


#problem 1
print("give me a whole number")
number = input("> ")
factors = []
for x in range(1, int(number)+1):
    if(int(number)%x==0):
        factors.append(x)
print(number, " has ",len(factors)," factors. ",factors)

#problem 2
print("Type a word")
word = input("> ")
word_split = word.split(" ")
for x in word:
    if(x=="a"):
        print("Alpha")
    elif(x=="b"):
        print("Bravo")
    elif(x=="c"):
        print("Charlie")
    elif(x=="d"):
        print("Delta")
    elif(x=="e"):
        print("Echo")
    elif(x=="f"):
        print("Foxtrot")
    elif(x=="g"):
        print("Golf")
    elif(x=="h"):
        print("Hotel")
    elif(x=="i"):
        print("Indigo")
    elif(x=="j"):
        print("Juliet")
    elif(x=="k"):
        print("Kilo")
    elif(x=="l"):
        print("Lima")
    elif(x=="m"):
        print("Mike")
    elif(x=="n"):
        print("November")
    elif(x=="o"):
        print("Oscar")
    elif(x=="p"):
        print("Papa")
    elif(x=="q"):
        print("Quatar")
    elif(x=="r"):
        print("Romeo")
    elif(x=="s"):
        print("Siera")
    elif(x=="t"):
        print("Tango")
    elif(x=="u"):
        print("Uniform")
    elif(x=="v"):
        print("Victor")
    elif(x=="w"):
        print("Whiskey")
    elif(x=="x"):
        print("X-ray")
    elif(x=="y"):
        print("Yankee")
    elif(x=="z"):
        print("Zulu")
    else:
        print("Not word try english again")
