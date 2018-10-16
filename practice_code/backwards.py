backwards_sentence=""
sentence="The quick brown fox jumped over the lazy dog"
words=sentence.split(" ")
for x in words:
    backwards=x[::-1]
    backwards_sentence = backwards_sentence+" "
print(backwards_sentence)