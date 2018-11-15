def decode_ellen_speak(letters):
    count = 0
    seperate_letters = letters.split(" ")
    original = seperate_letters[count]
    current = seperate_letters[count+1]
    if(str(original)==str(current)):
        return seperate_letters.remove(current)
        count+=1
        decode_ellen_speak(letters)
    else:
        return decode_ellen_speak(letters)
        count+=1

print("please enter ellen noise (whale noise) > ")
word = input("> ")
decode_ellen_speak(word)
