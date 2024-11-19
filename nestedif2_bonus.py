# Task: Employee Bonus Calculator

positions = [(1,"ceo"),(2,"manager"),(3,"engineer"),(4,"clerk"),(5,"hod")]

print("keys | values")
print("-"*15)
print(f"{positions[0][0]}    | {positions[0][1]}")
print(f"{positions[1][0]}    | {positions[1][1]}")
print(f"{positions[2][0]}    | {positions[2][1]}")
print(f"{positions[3][0]}    | {positions[3][1]}")
print(f"{positions[4][0]}    | {positions[4][1]}")

choise = int(input("enter your choise : "))
bonus=0

if choise==1:
    salary = 200000
    year = int(input("enter service years : "))
    if year>10:
        bonus=0.25
        
    else:
        bonus=0.20
        
elif choise==2:
    salary = 100000
    year=int(input("enter service years : "))
    if year>5:
        bonus=0.20
        
    else:
        bonus=0.15
        
elif choise==3:
    salary=120000
    year = int(input("enter service years : "))
    if year>4:
        bonus = 0.15
        
    else:
        bonus = 0.10
        
elif choise==4:
    salary=20000
    year = int(input("enter your exeprience : "))
    if year>2:
        bonus=0.10
        
    else:
        bonus=0.7
        
elif choise==5:
    salary=50000
    year = int(input("enter your service years : "))
    if year>5:
        bonus=0.20
        
    else:
        bonus=0.15
        
else:
    print("invalid position")
    
print("increment : +",bonus,"%")
print("previous salary : ",salary)

bonus = (salary*bonus)
print("bonus : ",bonus)

print("new salary : ₹",salary+bonus)