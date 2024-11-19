# password strenth tracker

password = input("enter password : ")

print("password : ",password)
password = list(password)
lower = False
upper = False
digit = False

for i in password:
    if i.islower() == True:
        lower=True
        
    elif i.isupper() == True:
        upper=True
        
    elif i.isdigit() == True:
        digit = True
            

if "@" in password or "#" in password or "_" in password or "&" in password or "$" in password:
    symbol=True
    
else:
    symbol = False
    
length = len(password)

# print(length,lower,upper,digit)

if length>10 and lower==True and upper==True  and symbol==True:
    print("this is strong password")
    
elif length>6 and length<=10 and lower==True :
    print("this is modrate password")
    
else:
    print("this is low password")