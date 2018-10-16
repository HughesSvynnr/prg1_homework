'''
a strong number is defined as a number that has the sum of the factorial of
each digit is equal to its original number
'''
for number_to_check in range(10000001):
    snumber = str(number_to_check)
    #get all of the digits (split)
    sum = []
    #calculate factorial for each digit
    for digit in snumber:
        factorial = 1
        for number in range(1,int(digit)+1):
            factorial = number * factorial
        sum.append(factorial)


    #add all factorials together
    final_factorial = 0
    for number in sum:
        final_factorial += number
    #check if the sum is same as original

    if(final_factorial ==  snumber):
        print(snumber + " is number is strong")