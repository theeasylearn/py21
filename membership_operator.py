# membership operator 
# in and not in
# true - 1 and false - 0
l1 = [0,2,3,4,5,6,7,8,9,10]

check = 10 in l1
print(check)

print(110 in l1)
print("red" in l1)
print(True in l1)
print(False in l1)

t1 = ("red",1,True,9.8)
print(True in t1)

element = (input("enter value : "))    #int(input("message")) convert type of input
print("status : ",element in t1)

numbers = {"no1" : 1,"no2":2,"no3":3}

print("no1" in numbers.items())
print(numbers.items())

print("red" not in t1)
print("1" not in t1)   # 1 in convert in str 