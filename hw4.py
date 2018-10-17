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
'''
#problem 2
print("Type a word")
word = input("> ")
word_split = word.split(" ")
for x in word:
'''