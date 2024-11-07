# swap 2 variable

#with using third variable 
a=input("enter first variable : ")
b=input("enter second variable : ")
print("before swap")
print("a :",a)
print("b :",b)

c = a
a=b
b=c

print("after swap") 
print("a :",a)
print("b :",b)

#without using third variable -------------------------------------------
a=input("enter first variable : ")
b=input("enter second variable : ")
print("before swap")
print("a :",a)
print("b :",b)

a,b = b,a

print("after swap")
print("a :",a)
print("b :",b)