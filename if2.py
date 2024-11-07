# find gretest number amoung 2 numbers

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

if a>b:
    print("number 1 is gretest")
    
if b>a :
    print("number 2 is gretest")
    
if a==b:
    print("both are same...")
    
# -------------------------------------------------------------------- 
print("\n")   
l1 = ["red","green","yellow","blue"]
value = input("enter value : ")

# f string
if value in l1:
    # print(value,"founded in list at index : ",l1.index(value))
    print(f"{value} founded in list at index : {l1.index(value)}")  #f string
    
if value not in l1:
    # print(value,"not founded in list")
    print(f"{value} not founded in list")
    
