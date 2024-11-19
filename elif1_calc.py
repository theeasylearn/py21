# write a program that make calculations
print("1 -> addition\n2 -> subtraction\n3 -> multiplication\n4 -> division")

number = int(input("enter number : "))

if number==1:
    a=float(input("enter number1 : "))
    b=float(input("enter number2 : "))
    print(a+b)
    
elif number==2:
    a=float(input("enter number1 : "))
    b=float(input("enter number2 : "))
    print(a-b)
    
elif number==3:
    a=float(input("enter number1 : "))
    b=float(input("enter number2 : "))
    print(a*b)
    
elif number==4:
    a=float(input("enter number1 : "))
    b=float(input("enter number2 : "))
    print(a/b)
    
else:
    print("error : invalid input")