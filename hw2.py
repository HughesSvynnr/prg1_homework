# prg2_Homework
#problem 1

p = int(input("how many people are coming to the fire at the beach? "))

if(p == 1):
    print("Just you then?")

elif(p == 2):
    print("Bring mashmallows")

elif(p >= 3,6):
    print("More than 3 is a crowd")

elif(p >= 7):
    print:("PARTAAAAAAAAY")

elif(p == 0):
    print:("You have no choice.")


#problem 2

print("You are driving a little too fast, and a police man stops you.")

sl = int(input("What is the speed limit? "))

s = int(input("How fast were you going? "))

b = input("Is it your birthday? ")

if(b == "yes"):
    print("Heppy birfdey")
    sl = (sl - 5)

if(s <= sl):
    print("Have a nice day")

elif(s >= sl*2):
    print("Give me your liscens now.")

elif(s <= (sl + 5)):
    print("This is your warning")

elif(s <= (sl + (5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15))):
    print("heres a small ticket.")

elif(s <= (sl + 15)):
    print("Big ticket for you")