#1.create a lambda function that multiplies argument x with argument y
a=lambda x,y : x*y
print(a(2,5))
#2.create fibonacci series to n using lambdafrom functools import reduce
from functools import reduce
a=int(input("enter a value:"))
f_series=lambda a: reduce(lambda x,_: x+[x[-1] + x[-2]],range(a - 2),[0, 1])
print(f_series(a))
#3.multiply each number of given list with a given number
list=[2,4,6,8]
a=int(input("Enter a value:"))
Newlist= [i*a for i in list]
print(Newlist)
#4.find numbers divisible by 9 from a list of numbers
my_list=[2,4,6,8,10,12,16]
result=list(filter(lambda x: (x % 4 == 0),my_list))
print("Numbers divisible by 4:",result)
#5.count even numbers in a given list of integers
lista=[2,3,5,6,8,9]
r= list(filter(lambda x: (x%2 == 0),lista))
print(r)
print("Number of even numbers in lista :",len(r))