numbers=input("enter 10 numbers with a comma inbetween > ")
numbers_count=len(numbers)


print(numbers)

numbers_list=numbers.split(",")

numbers_count=len(numbers_list)

half=int(numbers_count/2)

print(numbers_list)

last_half=numbers_list[half:numbers_count]

print(last_half)

first_half=numbers_list[0:half]

print(first_half)

print(numbers_list[1:8])

print(numbers_list[::-1])#reverse the order

reverse_numbers=",".join(numbers_list[::-1])

print(reverse_numbers)


'''
import matplotlib.pyplot as plt

xlist=[0,1,2,3,4,5]
ylist=[0,1,4,9,16,25]
x=[1,2,3,4,5]
y=[1,4,9,16,25] 

plt.title("y=x**2")
plt.plot(xlist,ylist)
plt.show()

input("press enter")
'''