cars = {1:"Sedan",2:"SUV",3:"Electric"}
l1=list(cars.keys())

print("keys\t\tvalues")
print("-"*40)
print(f"{l1[0]}\t\t{cars[1]}")
print(f"{l1[1]}\t\t{cars[2]}")
print(f"{l1[2]}\t\t{cars[3]}")

choise = int(input("enter your choise : "))

if choise==1:
    ch = int(input("1 for luxury or 2 for not : "))
    
    if ch==1:
        print("premium petrol")
        
    elif ch==2:
        print("regular petrol")
        
    else:
        print("choise not valid")
        
elif choise==2:
    ch = int(input("1 for diesel or 2 for petrol car : "))
    if ch==1:
        print("diesel")
        
    elif ch==2:
        print("petrol")
        
    else:
        print("invalid choise")
        
elif choise==3:
    ch = (input("you have electric charging station(y/n) : "))
    if ch=="y":
        print("electric charging is ready")
        
    else:
        print("not available")


else:
    print("unknown car type") 
       
    