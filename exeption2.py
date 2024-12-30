try:
    a=int(input("enter ele1 : "))
    b=int(input("enter ele2 : "))
    c=int(input("enter ele3 : "))
    d=int(input("enter ele4 : "))

    print(str(a)+b+c+d)

except ValueError:
    print("error : give right type of value!!!")
    
except (TypeError ,KeyboardInterrupt):
    print(TypeError)
    
# except Exception as e:
#     print(e)

finally:
    print("important code....")
    
try:
    n = int(input("enter number : "))
    if n<18:
        raise ValueError

except ValueError:
    print("below 18 is not valid!!!")
