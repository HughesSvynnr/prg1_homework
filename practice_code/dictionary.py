word = input("enter a word ")
lettercount={}#dictionary

for letter in word:
    if(letter in lettercount):
        lettercount[letter]+= 1
    else:
        lettercount[letter]=1
print(lettercount["t"])
