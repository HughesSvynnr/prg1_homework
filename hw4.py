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
print("Please pick a whole number")
number = input("> ")
number_2 = (number%(number))
for number in range(100): 
    print(number % number_2)
'''
#problem 2
print("type a word ")
word = input("> ")
'''
'''
max = [0,1,2,3,4]
for count in max:
    print(count)

for x in range(5):
    print(x**2)
'''