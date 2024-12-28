# default argument
def student(name="unknown",cls=0,roll=0,age=0,mobile=0):
    print("name : ",name)
    print("class : ",cls)
    print("roll no : ",roll)
    print("age : ",age)
    print("mobile no : ",mobile)
    
student("devarsh",12,323,17)
student()
print()

# keyword argument
def marks(eng,maths,science):
    print("english : ",eng)
    print("maths : ",maths)
    print("science : ",science)
    
marks(10,45,20)
marks(science=20 , maths=45 , eng=10)

# return multiple value
def getmultiple(n,m):
    return n,m

print(getmultiple(10,20))

# arbitary argument
def sum(*n):
    add = 0 
    for i in n:
        add = add+i
        
    return add

l1=[]
while True:
    n = int(input("enter number : "))
    l1.append(n)
    
    choise = int(input("enter 0 for stop and 1 for continue : "))
    if choise==0:
        break
    else:
        continue
    
# l1=str(l1)
# l1[0] = ""
# l1[len(l1)-1]=""
print(sum(l1[0],l1[1]))
# print(sum(10,20,30))
# print(sum(10,20,30,30303,3303))

# lamda function
even = lambda n : n%2 == 0
print(even(10))