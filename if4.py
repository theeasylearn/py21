a=int(input("enter number1 : "))
b=int(input("enter number2 : "))
c=int(input("enter number3 : "))

# a>b a>c
if a>b and a>c:
    print("a is max")
    
if b>a and b>c:
    print("b is max")
    
if c>a and c>b:
    print("c is max")
    
if a==b and a==c:
    print("all are same")