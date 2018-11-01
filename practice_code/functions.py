'''def add_numbers():
    number1 = 2
    number2 = 3
    total = number1 + number2
    print(total)
add_numbers()


def number_in_range(low,high,number):
    if(low < number and high > number):
        return True
    else:
        return False

number1=1
number10=10
numberinrange=4
numberoutofrange=-5
numbertoohigh=100

isnumber1inrange=number_in_range(number1,number10,numberinrange)
print(isnumber1inrange)

number_in_range(number1,number10,numberinrange)
number_in_range(number1,number10,numberoutofrange)
number_in_range(number1,number10,numbertoohigh)
'''
'''
def make_unique(values):
    unique = []
    for value in values:
        if(not value in unique):
            unique.append(value)
    return unique

print(make_unique(input("enter values by a comma").split(",")))
'''


def a(list_num):
    list_num[0] +=1
def a1(b):
    a(b)
    a(b)
def a2(b):
    a1(b)
    a1(b)
def a3(b):
    a2(b)
    a2(b)

x=[0]
a3(x)
print(x)
