# import random
from random import *

# random return float between 0.0 and 1.0
print(random())
print(round(random(),2))

# uniform return float between 2 given number
print(uniform(10,20))
print(round(uniform(10,100),2))

# randint return only integer value between given 2 numbers
print(randint(1,10))

# randrange return integer value between given 2 number and with size
# randrange(start,stop,gap/size)
print(randrange(0,100,10))

# choise return a random element from list,tule,set,dict
color = ["red","green","blue","black"]
print(choice(color))

# s1 = {1,"python",3.14,True}
# print(choice(s1))             it shows error becuase set not support choise

d1 = {"a":1,"b":2,"c":3}
print(choice(list(d1.keys())))
print(choice(list(d1.values())))

# choices return more than 1 value from list
card = ("A","K","Q","J","1","2")
print(choices(card,k=3))

# shuffle method changes element position of list
l1=["a","b","c","d","e","f"]
print("before shuffle : ",l1)
shuffle(l1)
print("after shuffle : ",l1)

# sample return number of random value from list but duplicate values are not allowed
l1=["a","b","c","d","e","f","a","b"]
print(sample(l1,3))
print(l1)