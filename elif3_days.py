days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

print("give a number for days...")
choise = int(input("enter your choise : "))

if choise==1:
    print(days[0])
    
elif choise ==2:
    print(days[1])

elif choise==3:
    print(days[2])

elif choise==4:
    print(days[3])
    
elif choise==5:
    print(days[4])
    
elif choise==6:
    print(days[5])
    
elif choise==7:
    print(days[6])
    
else:
    print("error : choise not found")