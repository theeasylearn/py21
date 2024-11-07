num1 = 5.6
num2 = 100

# answer = num1+num2
#addition of 400 and 100 is 500 
print("addition of ",num1,"and",num2,"is",num1+num2)

print(type(num1))
print(type(num2))

balance = True
print(type(balance))

num2 = "100"
name = "hello world"
print(type(name))
print(len(name))
print(len(num2))

# slicing string
# print(variable_name[index])
print(name[0])
print(name[10])
print(name[4])

# print(variable_name[start=0 : end = last : size = 1])
print(name[0:3:1])
print(name[3:5:1])
print(name[6:11:2])

#hor
print(name[0:9+1:4])
print(name[5:11:5])
print(name[10::-1])
print(name[::])
print(name[::-1])